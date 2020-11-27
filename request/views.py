from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

#views của homepage
def home(request):
    context = {}
    return render(request,'requestit/index.html', context)

#create request
def create_request(request):
    context = {}
    return render(request,'requestit/create_request.html', context)
