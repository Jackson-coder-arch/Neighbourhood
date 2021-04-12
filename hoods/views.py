from django.shortcuts import render
from .models import NeighbourHood
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

    return render(request, 'hood.html',{'form':form})

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

    return render(request,'business.html',{'form':form})


