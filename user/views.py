from django.shortcuts import render
from django.http import HttpResponse
from .forms import *
# Create your views here.

def index(request):
    return HttpResponse("Hello, world. You're at the User index.")

def form(request):
    if request.method == "POST":
        print("HERE")
        return redirect('user:index')

    form = SampleForm()
    return render(request, 'user/form.html', {'form':form})

