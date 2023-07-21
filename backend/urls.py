"""djangoHeroku URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from .api import views
from .api.views import index_view, UserViewSet, GroupViewSet, MessageViewSet
from django.conf.urls.static import static
from .settings import base

router = routers.DefaultRouter()
router.register('messages', MessageViewSet)
router.register('users', UserViewSet)
router.register('groups', GroupViewSet)

urlpatterns = [
    # http://localhost:8000/api/<router-viewsets>
    path('api/', include(router.urls)),

    path('api/explorer/', include('rest_framework.urls', namespace='rest_framework')),
    
    path('api/checkUserKey/', views.UserKeyView, name="user-key-view"),
    path('api/registerUserKey/', views.RegisterKeyView, name="register-key-view"),
    
    path('api/checkUserSession/', views.UserSessionView, name="user-session-view"),
    
    path('api/getIdeaScore/', views.GetIdeaScoreView, name="get-idea-score"),
    path('api/getTestingInfo/', views.GetTestingInfoView, name="get-testing-info"),
    path('api/getObjectKey/', views.GetObjectKeyView, name="get-object-key"),
    path('api/getNextKey/', views.GetNextKeyView, name="get-next-key"),
    path('api/getIdeaList/', views.GetIdeaListView, name="get-idea-list"),
    path('api/getScoreList/', views.GetScoreListView, name="get-score-list"),
    path('api/setUserRound/', views.SetUserRoundView, name="set-user-round"),
    
    path('api/dj-rest-auth/', include('dj_rest_auth.urls')),
    path('api/dj-rest-auth/registration/', include('dj_rest_auth.registration.urls')),

    # http://localhost:8000/api/admin/
    path('api/admin/', admin.site.urls),
    
    # http://localhost:8000/
    path('', index_view, name='index'),

]