from django.shortcuts import render
from .models import Room

rooms =[
    {'id':1,'name':'Learn python'},
    {'id':2,'name':'Design with me'},
    {'id':3,'name':'Frontend developers'},
]

def home(request):
    rooms= Room.objects.all()
    return render(request,'base/home.html',{'rooms': rooms})

def room(request,pk):
    room = None
    for i in rooms:
        if i['id'] == int(pk):
            room = i
    context = { 'room' :room}    
    return render(request,'base/room.html',context)

