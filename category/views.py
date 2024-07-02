from django.shortcuts import render
from django.http import Http404
from .models import Category

# Create your views here.
def index(request) : 
    categories=Category.objects.all()
    return render(request,'index.html',{
        'categories':categories
    })
def show(request, id) :

    try :
        category = Category.objects.get(pk=id)
    except : 
        raise Http404()
    return render(request, 'show.html',{
        'category': category
    })