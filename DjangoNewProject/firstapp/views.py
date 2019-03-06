from django.shortcuts import render
from django.http import HttpResponse
from .forms import UseForm



def index(request, name = None, path = None):

    name = request.POST.get("name")
    path = request.POST.get('bb')

    if request.method == "POST":
        useform = UseForm()
        data = {'form':useform,"name": name, 'patch': path}
        return render(request, 'index.html',context=data)



# Create your views here.
