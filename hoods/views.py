from django.shortcuts import render,redirect
from django.http import HttpResponseRedirect
from .forms import NeighbourHoodForm,BusinessForm,ProfileForm
from .models import NeighbourHood,Business,Profile
# Create your views here.

def home(request):
    if request.method == 'GET':
        hood = NeighbourHood.get_info()
    return render(request, 'home.html',{'hood':hood})

def neighbourhood(request):
    if request.method == 'POST':

        form = NeighbourHoodForm(request.POST, request.FILES)
        if form.is_valid():
            print('form is valid')
            hood = form.save(commit=False)
            post.save()
            return redirect('home')
    else:
        form = NeighbourHoodForm()

    return render(request, 'neighbourhood.html',{'form':form})

def business(request):
    bizz = Business.get_info()
    if request.method == 'POST':
        form = BusinessForm(request.POST, request.FILES)
        if form.is_valid():
            bizz = form.save(commit=False)
            post.save()
            return redirect('business')
    else:
        form = BusinessForm()

    return render(request,'bizz.html',{'form':form})

def profile(request, prof_id):
    user = User.objects.filter(pk=prof_id )
    profile = Profile.objects.filter(user= prof_id)

    return render(request, 'profile.html', {"profile" : profile}) 

def updateProfile(request,username):
    if request.method == 'POST':
        form = ProfileForm(request.POST,request.FILES, instance=request.user.profile)
        
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(request.path_info)
    else:
        form = ProfileForm(instance=request.user.profile)
     

    return render(request,'profile.html',{'form':form})

def details(request):
    return render(request,'details.html')