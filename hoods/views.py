from django.shortcuts import render

# Create your views here.
def home(request):
    if request.method == 'GET':
        hood = NeighbourHood.get_info()
    return render(request, 'home.html',{'hood':hood} )
