from django.db import models

class User(models.Model):
    name     = models.CharField(max_length=100)
    email    = models.EmailField(max_length=200,unique=True)
    password = models.CharField(max_length=50)
    mobile_no = models.CharField(max_length=10)
    date_created = models.DateTimeField(auto_now=True)
    
class Game(models.Model):
    name = models.CharField(max_length = 150)
    image = models.CharField(max_length=1000)
    prize = models.CharField(max_length=1000)
    startdate = models.CharField(max_length=50)
    enddate = models.CharField(max_length=50)
    starttime = models.CharField(max_length=50)
    endtime  = models.CharField(max_length=50)
    points = models.CharField(max_length=50)
    questionscount = models.CharField(max_length=50)
    user_id = models.IntegerField()
    date_created = models.DateTimeField(auto_now=True)

class QuestionAnswer(models.Model):
    game_id = models.IntegerField()
    question = models.TextField()
    answer  = models.TextField()
    date_created = models.DateTimeField(auto_now=True)
    
class Player(models.Model):
    name     = models.CharField(max_length=100)
    email    = models.EmailField(max_length=200,unique=True)
    password = models.CharField(max_length=50)
    mobile_no = models.CharField(max_length=10)
    date_created = models.DateTimeField(auto_now=True)
class Pointstable(models.Model):
    points = models.IntegerField()
    game_id = models.IntegerField()
    player_id = models.IntegerField()
    date_created = models.DateTimeField(auto_now=True)
    