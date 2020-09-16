from django.shortcuts import render
from django.conf import settings
from django.core.files.storage import FileSystemStorage
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.http.response import JsonResponse
from django.core import serializers
from .models import User,QuestionAnswer,Game,Player,Pointstable
import json
import random
@csrf_exempt
def simple_upload(request,*args,**kwargs):
    myfile=request.FILES['files']
    fs = FileSystemStorage()
    filename = fs.save(myfile.name, myfile)
    uploaded_file_url = fs.url(filename)
    return HttpResponse(uploaded_file_url)
@csrf_exempt
def newgame(request,user_id):
    body = json.loads(request.body)
    game = Game(name=body["name"],image=body["image"],startdate=body["startdate"],enddate=body["enddate"],starttime=body["starttime"],endtime=body["endtime"],prize=body["prize"],points=body["points"],questionscount=body["questions"],user_id=user_id)
    game.save()
    game_id = game.pk
    for i,j in enumerate(body["pictures"]):
        qa = QuestionAnswer(question=j,answer=body["answers"][i],game_id=game_id)
        qa.save()
    game = Game.objects.filter(pk=game_id)
    serialized_queryset = serializers.serialize('json', game)
    return HttpResponse(serialized_queryset)
@csrf_exempt
def signup(request):
    body = json.loads(request.body)
    if len(body["mobile"])>10:
        return JsonResponse("Mobile",safe=False)
    else:
        users = User.objects.filter(email=body["email"])
        if len(users)==0:
            s = User(email=body["email"],name=body["name"],password=body["password"],mobile_no=body["mobile"])
            s.save()
            print(s)
            get = User.objects.filter(email=body["email"])
            serialized_queryset = serializers.serialize('json', get)
            return HttpResponse(serialized_queryset)
        else:
            print("User Exist")
            return JsonResponse("User",safe=False)
@csrf_exempt
def login(request):
    body = json.loads(request.body)
    print(body["password"])
    users = list(User.objects.filter(email=body["email"]))
    if len(users)!=0:
        if users[0].password==body["password"]:
            serialized_queryset = serializers.serialize('json', users)
            return HttpResponse(serialized_queryset)
        else:
            print("Password incorrect")
            return JsonResponse("Password",safe=False)
    else:
        print("User Doesn't exists")
        return JsonResponse("User",safe=False)
@csrf_exempt
def getgames(request,user_id):
    print(request.method)
    game = Game.objects.filter(user_id=user_id)
    serialized_queryset = serializers.serialize('json', game)
    return HttpResponse(serialized_queryset)
@csrf_exempt
def getgamebyid(request,game_id):
    print(game_id)
    game = Game.objects.filter(pk=game_id)
    questions = QuestionAnswer.objects.filter(game_id=game_id)
    serialized_queryset = serializers.serialize('json', game)
    serialized_queryset1 = serializers.serialize('json', questions)
    return HttpResponse(json.dumps({"game":serialized_queryset,"question":serialized_queryset1}))

@csrf_exempt
def signupplayer(request):
    body = json.loads(request.body)
    if len(body["mobile"])>10:
        return JsonResponse("Mobile",safe=False)
    else:
        users = Player.objects.filter(email=body["email"])
        if len(users)==0:
            s = Player(email=body["email"],name=body["name"],password=body["password"],mobile_no=body["mobile"])
            s.save()
            print(s)
            get = Player.objects.filter(email=body["email"])
            serialized_queryset = serializers.serialize('json', get)
            return HttpResponse(serialized_queryset)
        else:
            print("User Exist")
            return JsonResponse("User",safe=False)
@csrf_exempt
def loginplayer(request):
    body = json.loads(request.body)
    print(body["password"])
    users = list(Player.objects.filter(email=body["email"]))
    if len(users)!=0:
        if users[0].password==body["password"]:
            serialized_queryset = serializers.serialize('json', users)
            return HttpResponse(serialized_queryset)
        else:
            print("Password incorrect")
            return JsonResponse("Password",safe=False)
    else:
        print("User Doesn't exists")
        return JsonResponse("User",safe=False)
    
@csrf_exempt
def allgamesforplayer(request):
    allgames = Game.objects.all()
    allquestions = []
    sendtobackend = []
    objtoappend = {}
    for i in allgames:
        objtoappend = {}
        allquestions.append(QuestionAnswer.objects.filter(game_id=i.pk))
        objtoappend["name"] = i.name
        objtoappend["pk"] = i.pk
        objtoappend["image"] = i.image
        objtoappend["startdate"] = i.startdate
        objtoappend["enddate"] = i.enddate
        objtoappend["starttime"] = i.starttime
        objtoappend["endtime"] = i.endtime
        objtoappend["prize"] = i.prize
        objtoappend["points"] = i.points
        objtoappend["questionscount"] = i.questionscount
        objtoappend["questions"] = []
        objtoappend["answers"] = []
        sendtobackend.append(objtoappend)
    for index,j in enumerate(allquestions):
        for k in range(len(j)):
            some ={}
            some1 = {}
            some["pk"] = j[k].pk
            some1["pk"] = j[k].pk
            some["question"] = j[k].question
            jumbled = list(j[k].answer)
            random.shuffle(jumbled)
            listToStr = ''.join([str(elem) for elem in jumbled])
            some1["answer"] = listToStr
            sendtobackend[index]["questions"].append(some)
            sendtobackend[index]["answers"].append(some1)
    return JsonResponse(sendtobackend,safe=False) 

@csrf_exempt
def checkanswer(request,gameid):
    body = json.loads(request.body)
    print(gameid)
    fromdatabase = QuestionAnswer.objects.get(pk=gameid)
    answer = fromdatabase.answer
    print(body["answer"].lower())
    print(answer.lower())
    if body["answer"].lower()==answer.lower():
        print("correct")
        return JsonResponse("correct",safe=False)
    else:
        print("wrong")
        return JsonResponse("wrong",safe=False)
    
@csrf_exempt
def addpoints(request):
    body = json.loads(request.body)
    print(body)
    s = Pointstable(points=body["points"],game_id=body["gameid"],player_id=body["userid"])
    s.save()
    return JsonResponse("successfully saved",safe=False)

@csrf_exempt
def getwinner(request,gameid):
    print(gameid)
    data = Pointstable.objects.filter(game_id=gameid).order_by('-points')
    send = []
    for i in data:
        state ={}
        name = Player.objects.get(pk=i.player_id)
        state["name"] = name.name
        state["email"] =name.email
        state["points"] = i.points
        send.append(state)
    print(send)
    return JsonResponse(send,safe=False)