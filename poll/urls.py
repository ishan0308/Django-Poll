from django.urls import path,re_path
from . import views

urlpatterns = [
    path('',views.index,name='index'),
    path('addpoll',views.addpoll,name='addpoll'),
    path('tpoll',views.tpoll,name='tpoll')
]
