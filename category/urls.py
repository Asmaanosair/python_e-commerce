from django.urls import path
from . import views
urlpatterns = [
    path('',views.index,name='category'),
    path('show/<int:id>',views.show,name='show_category')
]
