from django.urls import path
from . import views

urlpatterns = [
    path('',views.index,name='index'),
    path('signup/',views.sign_up,name='signup'),
    path('signin/',views.sign_in,name='signin'),
    path('logout/',views.log_out,name='logout')
]
