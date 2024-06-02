from django.shortcuts import render
from django.http import HttpResponseNotFound

# Create your views here.
def index(request) : 
    return render(request,'index.html')
def custom_404(request, exception):
    return render(request, '404.html', status=404)

