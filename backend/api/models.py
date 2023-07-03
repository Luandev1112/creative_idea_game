from django.db import models

class Message(models.Model):
    subject = models.CharField(max_length=200)
    body = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
class IdeaMarks(models.Model):
    user_id = models.IntegerField()
    round = models.IntegerField()
    object_index = models.IntegerField(default=0)
    object = models.CharField(max_length=200)
    response = models.TextField()
    score = models.DecimalField(max_digits=2, decimal_places=1)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
class UserKey(models.Model):
    user_id = models.IntegerField()
    user_key = models.CharField(max_length=50)
    prolific_id = models.CharField(max_length=50, default=None)
    user_session = models.CharField(max_length=155, default=None)
    key_type = models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
class ObjectKeys(models.Model):
    round = models.IntegerField()
    object_key = models.CharField(max_length=155)

class UserRound(models.Model):
    user_id = models.IntegerField()
    round = models.IntegerField()
    object_index = models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)