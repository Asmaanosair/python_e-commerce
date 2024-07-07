from django.shortcuts import render
from django.http import Http404
from .models import Category
from django.shortcuts import get_list_or_404, get_object_or_404,redirect
import random
# Create your views here.
def index(request) : 
    categories=Category.objects.all()
    total=categories.count()
    return render(request,'index.html',{
        'categories':categories,
        'total':total
    })
def show(request, slug) :

    # try :
    #     category = Category.objects.get(pk=id)
    # except : 
    #     raise Http404()
    category= get_object_or_404(Category,slug=slug);
    return render(request, 'show.html',{
        'category': category
    })
def delete(request,id) :
    category = get_object_or_404(Category, id=id)
    category.delete()
    return redirect('categories')
def store(request) :
    name='cat_'+ str(random.randint(1, 100))
    Category.objects.create(name=name,active=True,slug=name)
    return redirect('categories') 