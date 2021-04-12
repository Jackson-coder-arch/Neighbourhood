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

