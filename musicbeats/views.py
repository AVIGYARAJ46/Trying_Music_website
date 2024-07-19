from django.shortcuts import render
from musicbeats.models import Song
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from django.shortcuts import redirect

def index(request):
    song=Song.objects.all()
    return render(request, 'index.html',{'song':song})

def search(request):
    query=request.GET.get("query")
    song = Song.objects.all()
    qs = song.filter(name=query)

    return render(request, 'musicbeats/search.html',{"songs":qs})



def watchlater(request):
    return render(request, 'musicbeats/watchlater.html')

def songs(request):
    song=Song.objects.all()
    return render(request, 'musicbeats/songs.html',{'song':song})

def songpost(request,id):
    song=Song.objects.filter(song_id=id).first()
    return render(request, 'musicbeats/songpost.html',{'song':song})

def login(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        from django.contrib.auth import login
        login(request, user)
        redirect('/')
    return render(request, 'musicbeats/login.html')

def signup(request):
    if request.method == "POST":
        email = request.POST['email']
        username = request.POST['username']
        first_name = request.POST['firstname']
        last_name = request.POST['lastname']
        password1 = request.POST['password1']
        password2 = request.POST['password2']

        myuser = User.objects.create_user(username, email, password1)
        myuser.first_name = first_name
        myuser.last_name = last_name
        myuser.save()
        user = authenticate(username=username, password=password1)
        from django.contrib.auth import login
        login(request, user)

        return redirect('/')
    return render(request, 'musicbeats/signup.html')

