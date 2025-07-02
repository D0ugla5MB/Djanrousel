from django.urls import path
from . import views

urlpatterns = [
    path('', '', name='home'),
    path('signin/', '', name='signin'),
    path('signup/', '', name='signup'),
    path('signout/', '', name='signout'),
    path('<str:username>/','',name='profile'),
    path('<str:username>/collection/','', name='collection'),
    path('<str:username>/collection/carousel/<str:carousel_id>',name='carousel_instance'),
    path('<str:username>/collection/carousel/<str:carousel_id>/<str:photo>', name='photo')
]