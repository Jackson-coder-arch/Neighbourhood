from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponseRedirect
from .forms import NeighbourHoodForm,BusinessForm,ProfileForm,PostsForm
from .models import NeighbourHood,Business,Profile,Posts
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib.auth import logout




def home(request):
    if request.method == 'GET':
        hood = NeighbourHood.get_info()
    return render(request, 'home.html',{'hood':hood})

@login_required(login_url='/accounts/login/')
def neighbourhood(request):
    if request.method == 'POST':

        form = NeighbourHoodForm(request.POST, request.FILES)
        if form.is_valid():
            print('form is valid')
            hood = form.save(commit=False)
            post.save()
            return redirect('hoods:home')
    else:
        form = NeighbourHoodForm()

    return render(request, 'neighbourhood.html',{'form':form})

# @login_required(login_url='/accounts/login/')
# def business(request):
#     bizz = Business.get_info()
#     if request.method == 'POST':
#         form = BusinessForm(request.POST, request.FILES)
#         if form.is_valid():
#             bizz = form.save(commit=False)
#             post.save()
#             return redirect('business')
#     else:
#         form = BusinessForm()

#     return render(request,'bizz.html',{'form':form})

def profile(request, prof_id):
    user = User.objects.filter(pk=prof_id )
    profile = Profile.objects.filter(user= prof_id)
    if request.method =='POST':
        form = ProfileForm(request.POST, request.FILES, instance=request.user.profile)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(request.path_info)
    else:
        form = ProfileForm(instance=request.user.profile)
    params = {
        'form': form,
        "profile" : profile
    }
    return render(request, 'profile.html', params)

@login_required(login_url='/accounts/login/')
def updateProfile(request,username):
    if request.method == 'POST':
        form = ProfileForm(request.POST,request.FILES, instance=request.user.profile)
        
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(request.path_info)
    else:
        form = ProfileForm(instance=request.user.profile)
     
    return render(request,'profile.html',{'form':form})
    
# @login_required(login_url='/accounts/login/')
# def posts(request,id=id):
#     post = Posts.get_info()
#     if request.method == 'POST':
#         form = PostsForm(request.POST,request.FILES)
#         if form.is_valid():
#             post = form.save(commit=False)
#             post.save()
#             return redirect('hoods:details',post.id)
#     else:
#         form =PostsForm()
#     return render(request,'post.html',{'form':form})
    
    
@login_required(login_url='/accounts/login/')
def details(request,id):
    hood = get_object_or_404(NeighbourHood, id=id)
    business = Business.objects.filter(estate=hood)
    posts= Posts.objects.filter(estate=hood)
    if request.method == 'POST':
        form = PostsForm(request.POST,request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.estate = hood
            post.user = request.user.profile
            post.save()
            return redirect('hoods:details',hood.id)
    else:
        form =PostsForm()
    if request.method == 'POST':
        b_form = BusinessForm(request.POST, request.FILES)
        if b_form.is_valid():
            bizz = b_form.save(commit=False)
            bizz.estate = hood
            bizz.user = request.user.profile    
            bizz.save()
            return redirect('hoods:details',hood.id)
    else:
        b_form = BusinessForm()

    context ={
        "hood":hood,
        "posts":posts,
        "business":business,
        "form":form,
        "b_form":b_form,
    }
    return render(request,'details.html',context)



def search_business(request):
    if request.method == 'GET':
        name = request.GET.get("business")
        results = Business.search_business(name)
        print(results)
        message = f'name'
        params = {
            'results': results,
            'message': message
        }
    
        return render(request,'search.html',params)
    
    else:
        message = "You haven't searched for any image category"
        
    return render(request,'search.html', {' message': message})

@login_required(login_url='/accounts/login/')
def join_hood(request, id):
    hood = get_object_or_404(NeighbourHood, id=id)
    request.user.profile.hood = hood
    request.user.profile.save()
    # messages.success(request, "Welcome to Your Hood!")
    return redirect('hoods:details', hood.id)


@login_required(login_url='/accounts/login/')
def leave_hood(request, id):
    hood = get_object_or_404(NeighbourHood, id=id)
    request.user.profile.hood = None
    request.user.profile.save()
    # messages.success(request, "Bye see you again")
    return redirect("hoods:home")    