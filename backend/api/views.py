from django.contrib.auth.models import User, Group
from django.views.generic import TemplateView
from django.views.decorators.cache import never_cache
from django.http import request
from django.http import HttpResponse
from rest_framework import viewsets, permissions
from rest_framework.views import APIView
from .models import Message
from .models import UserKey
from .models import IdeaMarks
from .models import ObjectKeys
from .models import UserRound
from .serializers import UserSerializer, GroupSerializer, MessageSerializer
import requests
from json import loads
from django.http import JsonResponse
import secrets
import random

# Serve Vue Application
index_view = never_cache(TemplateView.as_view(template_name='index.html'))

class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAdminUser]


class GroupViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
    permission_classes = [permissions.IsAdminUser]

class MessageViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows messages to be viewed or edited.
    """
    queryset = Message.objects.all()
    serializer_class = MessageSerializer
    # SHOULD IMPLEMENT CUSTOM PERMISSIONS FOR OBJECT LEVEL SECURITY
    
def UserKeyView(request, *args, **kwargs):
    user_status = 0
    key = request.POST.get('user_key', None)
    prolific_id = request.POST.get('prolific_id', None)
    if key != None:
        key_data = UserKey.objects.filter(user_key=key).filter(prolific_id=prolific_id)
        if key_data.count() > 0:
            random_string = secrets.token_hex(64)
            key_row = key_data[0]
            key_row.user_session = random_string
            key_row.save()
            request.session['user_session'] = random_string
            user_status = 1
            user_id = key_row.user_id
            scores_to_delete = IdeaMarks.objects.filter(user_id=user_id)
            scores_to_delete.delete()
            user_rounds = UserRound.objects.filter(user_id=user_id)
            if user_rounds.count() > 0:
                user_round = user_rounds[0]
                user_round.round = 1
                user_round.object_index = 1
                user_round.save()
            else:
                user_round = UserRound(user_id=user_id, round=1, object_index=1)
                user_round.save()
        else:
            user_status = 0
    return HttpResponse(user_status)

def UserSessionView(request):
    session_data = request.session.get('user_session')
    key_data = UserKey.objects.filter(user_session=session_data)
    status = 0
    if key_data.count() > 0:
        status = 1
    else:
        status = 0
    data = {
        'status' : status
    }
    return JsonResponse(data)

def GetIdeaScoreView(request):
    input_string = request.POST.get('input_string', '')
    idea_text = request.POST.get('idea_text', '')
    round = request.POST.get('round', 1)
    
    objectkey_id = 1
    objectkeydata = ObjectKeys.objects.filter(round=round).filter(object_key=input_string)
    if objectkeydata.count() > 0:
        objectkey_id = objectkeydata[0].id    
    
    session_data = request.session.get('user_session')
    key_data = UserKey.objects.filter(user_session=session_data)
    responseData = {}
    if key_data.count() > 0:
        key_row = key_data[0]
        user_id = key_row.user_id
        url = "https://openscoring.du.edu/llm"
        data = {
            'model' : 'gpt-davinci-paper_alpha',
            'prompt' : idea_text,
            'input' : input_string,
            'input_type' : 'csv',
            'elab_method' : "none"
        }
        headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.0.0 Safari/537.36",
            "Host": "reserve.tokyodisneyresort.jp",
            "Origin": "https://openscoring.du.edu",
            'Accept': 'application/json, text/javascript, */*; q=0.01',
            'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
            'X-Requested-With': 'XMLHttpRequest',
            "Sec-Ch-Ua-Platform": "Windows",
            "Sec-Fetch-Dest":"empty",
            "Sec-Fetch-Mode":"cors",
            "Sec-Fetch-Site": "same-origin",
            "Accept-Encoding":"gzip, deflate, br",
            "Accept-Language" : "en-US,en;q=0.9,pt;q=0.8,ja;q=0.7",
            "Connection" : "keep-alive"
        }
        session = requests.Session()
        retries = requests.packages.urllib3.util.retry.Retry(total=5, backoff_factor=0.1)
        adapter = requests.adapters.HTTPAdapter(max_retries=retries)
        session.mount('https://', adapter)
        response = requests.post(url, data=data, headers=headers)
        result_data = loads(response.content)
        responseData['status'] = 'success'
        print("result data : ", result_data)
        if 'scores' in result_data:
            score_data = result_data['scores'][0]
            responseData['curretScore'] = score_data['originality'] 
            responseData['curretString'] = score_data['response'] 
            responseData['curretInput'] = score_data['prompt']
            responseData['data'] = True
            idea_row = IdeaMarks(user_id=user_id, round=round, object=score_data['response'], response=score_data['prompt'], score=score_data['originality'], object_index=objectkey_id )
            idea_row.save()
            user_round = UserRound.objects.get(user_id=user_id)
            user_round.round=round
            user_round.object_index = objectkey_id
            user_round.save()
        else:
            responseData['curretScore'] = random.randint(10, 50) / 10
            responseData['curretString'] = input_string
            responseData['curretInput'] = idea_text
            responseData['data'] = True
            idea_row = IdeaMarks(user_id=user_id, round=round, object=input_string, response=idea_text, score=responseData['curretScore'], object_index=objectkey_id )
            idea_row.save()
            user_round = UserRound.objects.get(user_id=user_id)
            user_round.round=round
            user_round.object_index = objectkey_id
            user_round.save()
    else:
        responseData['status'] = 'fail'
        
    return JsonResponse(responseData)

def GetTestingInfoView(request):
    session_data = request.session.get('user_session')
    key_data = UserKey.objects.filter(user_session=session_data)
    round = 1
    current_word_index = 0
    result = {}
    key_type = 0
    if key_data.count() > 0:
        key_row = key_data[0]
        user_id = key_row.user_id
        key_type = key_row.key_type
        result['key_type'] = key_type
        user_round = None
        user_rounds = UserRound.objects.filter(user_id=user_id)
        if user_rounds.count() == 0:
            user_round = UserRound(user_id=user_id, round=1, object_index=1)
            user_round.save()
        else:
            user_round = user_rounds[0]
        
        round = user_round.round
        roundRows = IdeaMarks.objects.filter(user_id=user_id).filter(round=round)
        if roundRows.count() == 0:
            result['isStart'] = False
        else:
            result['isStart'] = True
        current_word_index = user_round.object_index
        
        # check final object index
        roundObjects = ObjectKeys.objects.filter(round=round).order_by('-id')
        if roundObjects[0].id == current_word_index:
            result['isFinal'] = True
        else:
            result['isFinal'] = False
            
        objectKey = ObjectKeys.objects.get(id=current_word_index)
        ideaRows = IdeaMarks.objects.filter(user_id=user_id).filter(object_index=current_word_index)
        if ideaRows.count() > 0:
            round_row_count = ideaRows.count()
            ideaList = []
            if round_row_count > 0:
                idx = 0
                for idea in ideaRows:
                    score_class = ''
                    if idea.score < 1.7:
                        score_class = 'low-score'
                    elif idea.score >= 1.7 and idea.score < 3.4:
                        score_class = 'middle-score'
                    else:
                        score_class = "high-score"
                    score_percent = str(idea.score * 20) + "%"
                    idea_data = {
                        'id' : idx,
                        'object' : idea.object,
                        'prompt' : idea.response,
                        'score' : idea.score,
                        'score_class' : score_class,
                        'score_percent' : score_percent
                    }
                    ideaList.append(idea_data)
                    idx += 1
            result['idea_list'] = ideaList
        else:
            result['idea_list'] = []
        result['status'] = 1
    else:
        result['status'] = 0
        
    result['round'] = round
    result['object_index'] = current_word_index 
    result['object_key'] = objectKey.object_key
        
    return JsonResponse(result)

def GetObjectKeyView(request):
    round = request.POST.get('round', 1)
    session_data = request.session.get('user_session')
    key_data = UserKey.objects.filter(user_session=session_data)
    key_index = 0
    object_key = ''
    result = {}
    if key_data.count() > 0:
        if int(round) < 4:   
            key_row = key_data[0]
            user_id = key_row.user_id
            user_round = UserRound.objects.get(user_id=user_id)
            object_key = ObjectKeys.objects.get(id=user_round.object_index).object_key
            result['status'] = 1
            result['object_key'] = object_key
        else:
            result['status'] = 1
            result['object_key'] = ""
    else:
        result['status'] = 0
    
    return JsonResponse(result)

def GetNextKeyView(request):
    object_index = request.POST.get('object_index', 1)
    session_data = request.session.get('user_session')
    key_data = UserKey.objects.filter(user_session=session_data)
    object_key = ''
    result = {}
    if key_data.count() > 0:
        key_row = key_data[0]
        user_id = key_row.user_id
        user_round = UserRound.objects.get(user_id=user_id)
        user_round.object_index = object_index
        user_round.save()
        object_key = ObjectKeys.objects.get(id=user_round.object_index).object_key
        result['status'] = 1
        result['object_key'] = object_key
    else:
        result['status'] = 0
    
    return JsonResponse(result)

def GetIdeaListView(request):
    round = request.POST.get('round', 1)
    session_data = request.session.get('user_session')
    key_data = UserKey.objects.filter(user_session=session_data)
    result = {}
    if key_data.count() > 0:
        key_row = key_data[0]
        user_id = key_row.user_id
        roundRows = IdeaMarks.objects.filter(user_id=user_id).filter(round=round)
        round_row_count = roundRows.count()
        ideaList = []
        if round_row_count > 0:
            idx = 0
            for idea in roundRows:
                score_class = ''
                if idea.score < 1.7:
                    score_class = 'low-score'
                elif idea.score >= 1.7 and idea.score < 3.4:
                    score_class = 'middle-score'
                else:
                    score_class = "high-score"
                score_percent = str(idea.score * 20) + "%"
                idea_data = {
                    'id' : idx,
                    'object' : idea.object,
                    'prompt' : idea.response,
                    'score' : idea.score,
                    'score_class' : score_class,
                    'score_percent' : score_percent
                }
                ideaList.append(idea_data)
                idx += 1
            result['idea_list'] = ideaList
        else:
            result['idea_list'] = []
        result['status'] = 1
    else:
        result['status'] = 0
    
    return JsonResponse(result)

def GetScoreListView(request):
    round = request.POST.get('round', 1)
    session_data = request.session.get('user_session')
    key_data = UserKey.objects.filter(user_session=session_data)
    result = {}
    if key_data.count() > 0:
        key_row = key_data[0]
        user_id = key_row.user_id
        roundRows = IdeaMarks.objects.filter(user_id=user_id)
        round_row_count = roundRows.count()
        ideaList = []
        if round_row_count > 0:
            idx = 0
            for idea in roundRows:
                idea_data = {
                    'id' : key_row.prolific_id,
                    'code' : key_row.user_key,
                    'round' : idea.round,
                    'object' : idea.object,
                    'response' : idea.response,
                    'creativity score' : idea.score,
                }
                ideaList.append(idea_data)
                idx += 1
            result['score_list'] = ideaList
        else:
            result['score_list'] = []
        result['status'] = 1
    else:
        result['status'] = 0
    
    print("Result:::", result)
    return JsonResponse(result)

def SetUserRoundView(request):
    round = request.POST.get('round', 1)
    session_data = request.session.get('user_session')
    key_data = UserKey.objects.filter(user_session=session_data)
    result = {}
    if key_data.count() > 0:
        key_row = key_data[0]
        user_id = key_row.user_id
        user_rounds = UserRound.objects.filter(user_id=user_id)
        if user_rounds.count() > 0:
            user_round = user_rounds[0]
            user_round.round = round
            user_round.object_index += 1
            user_round.save()
        result['status'] = 1
    else:
        result['status'] = 0
    return JsonResponse(result)       