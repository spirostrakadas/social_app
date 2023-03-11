from django.http import JsonResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serialiazers import ProfileSerializer,PostSerializer 
from core.models import Profile,Post

@api_view(['GET'])
def getRoutes(request):
    routes=[
        {'GET':'api/profiles'},
        {'GET':'api/profiles/id'},
        {'GET':'api/posts'},
        {'GET':'api/posts/id'},



        {'POST':'api/users/token'},
        {'POST':'api/users/token/refresh'}
        
    ]
    return Response(routes)


@api_view(['GET'])
def getProfiles(request):
    profiles=Profile.objects.all()
    serializer=ProfileSerializer(profiles,many=True)
    return Response(serializer.data)

@api_view(['GET'])
def getPosts(request):
    posts=Post.objects.all()
    serializer=PostSerializer(posts,many=True)
    return Response(serializer.data) 

@api_view(['GET'])
def getProfile(request,pk):
    profile=Profile.objects.get(id=pk)
    serializer=serializer=ProfileSerializer(profile,many=False)
    return Response(serializer.data) 

@api_view(['GET'])
def getPost(request,pk):
    post=Post.objects.get(id=pk)
    serializer=PostSerializer(post,many=False)
    return Response(serializer.data)
