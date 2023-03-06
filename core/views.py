from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib.auth.models import User,auth
from django.contrib import messages
from .models import Profile,Post,LikePost
from django.contrib.auth.decorators import login_required
# Create your views here.

@login_required(login_url='signin')
def index(request):
    user_object=User.objects.get(username=request.user.username)
    user_profile=Profile.objects.get(user=user_object)
    post=Post.objects.all()
    posts=Post.objects.all()
    return  render(request,'index.html',{'user_profile':user_profile,"post":post,'posts':posts})



def sign_up(request):

    if request.method == 'POST':
        username=request.POST['username']
        email=request.POST['email']
        password=request.POST['password']
        password2=request.POST['password2']

        if password ==password2:
            if User.objects.filter(email=email).exists():
                messages.info(request,'Email taken!')
                return redirect('signup')
            elif User.objects.filter(username=username).exists():
                messages.info(request,'Username taken,try another username!')
                return redirect('signup')
            else:
                user=User.objects.create_user(username=username,email=email,password=password)
                user.save()
                #log user in redirect seeting page
                user_login=auth.authenticate(username=username,password=password)
                auth.login(request,user_login)

                #create a profile object for a new user
                user_model=User.objects.get(username=username)
                new_profile=Profile.objects.create(user=user_model,id_user=user_model.id)
                new_profile.save()
                return redirect('signup')

                

        else:
            messages.info(request,'Password not matching')
            return redirect('signup')

    else:
        return render(request,'signup.html')

def sign_in(request):
    if request.method=="POST":
        username=request.POST['username']
        password=request.POST['password']
        user=auth.authenticate(username=username,password=password)

        if user is not None:
            auth.login(request,user)
            return redirect('/')
        else:
            messages.info(request,"crendentials invalid")

    else:
        return render(request,'signin.html')
    
@login_required(login_url='signin')
def log_out(request):
    auth.logout(request)
    return redirect('signin')


@login_required(login_url='signin')
def settings(request):

    user_profile=Profile.objects.get(user=request.user)
    if request.method== "POST":

        if request.FILES.get('image') == None:
            image=user_profile.profile_img
            bio=request.POST['bio']
            location=request.POST['location']

            user_profile.profile_image=image
            user_profile.bio=bio
            user_profile.location=location
            user_profile.save()

        if request.FILES.get('image') != None:
            image=request.FILES.get('image')
            bio=request.POST['bio']
            location=request.POST['location']

            user_profile.profile_image=image
            user_profile.bio=bio
            user_profile.location=location
            user_profile.save()
            return redirect('settings')


    return render(request,'settings.html',{'user_profile':user_profile})

@login_required(login_url='signin')
def upload(request):
    if request.method=="POST":
        user=request.user.username
        image=request.FILES.get('image_upload')#action='image_upload' in the html template!
        caption=request.POST['caption']

        new_post=Post.objects.create(user=user,image=image,caption=caption)
        new_post.save()
        return redirect("/")
    else:
        return redirect('/')
    
@login_required(login_url='signin')
def like_post(request):
    username=request.user.username
    post_id=request.GET.get('post_id')

    post=Post.objects.get(id=post_id)

    like_filter=LikePost.objects.filter(post_id=post_id,username=username).first()

    if like_filter == None:
        new_like = LikePost.objects.create(post_id=post_id,username=username)
        new_like.save()
        post.number_of_likes=post.number_of_likes+1
        post.save()
        return redirect('/')
    else:
        like_filter.delete=post.number_of_likes-1
        post.save()
        return redirect('/')
