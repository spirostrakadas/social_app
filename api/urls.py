from django.urls import path
from . import views

urlpatterns = [
    path('',views.getRoutes),
    path('profiles/',views.getProfiles),
    path('posts/',views.getPosts),
    path('profiles/<str:pk>/',views.getProfile),

]
