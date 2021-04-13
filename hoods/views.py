from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponseRedirect
from .forms import NeighbourHoodForm,BusinessForm,ProfileForm,PostsForm
from .models import NeighbourHood,Business,Profile,Posts




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
            return redirect('hoods:home')
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
    

def posts(request):
    post = Posts.get_info()
    if request.method == 'POST':
        form = PostsForm(request.POST,request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.save()
            return redirect('details',hood.id)
    else:
        form =PostsForm()
    return render(request,'post.html',{'form':form})
    
    

def details(request,id):
    hood = NeighbourHood.objects.get(id=id)
    business = Business.objects.filter(estate=hood)
    posts= Posts.objects.filter(estate=id).order_by('-post')
   

    context ={
        "hood":hood,
        "posts":posts,
        "business":business
    }
    return render(request,'details.html',context)



def search_business(request):
    if request.method == 'GET':
        name = request.GET.get("title")
        results = Business.objects.filter(name__icontains=name).all()
        print(results)
        message = f'name'
        params = {
            'results': results,
            'message': message
        }
    
        return render(request,'search.html')
    
    else:
        message = "You haven't searched for any image category"
        
    return render(request,'search.html')

def join_hood(request, id):
    hood = get_object_or_404(NeighbourHood, id=id)
    request.user.profile.hood = hood
    request.user.profile.save()
    # messages.success(request, "Welcome to Your Hood!")
    return redirect('hoods:details', hood.id)

def leave_hood(request, id):
    hood = get_object_or_404(NeighbourHood, id=id)
    request.user.profile.hood = None
    request.user.profile.save()
    # messages.success(request, "Bye see you again")
    return redirect("hoods:home")    