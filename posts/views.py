from django.shortcuts import redirect, render
from django.http import HttpResponse, HttpResponseRedirect
from .models import Post
from .forms import PostForm

# Create your views here.
def index(request):
    #if the method is POST
    if request.method == 'POST':
        form = PostForm(request.POST)
        #if the form is valid
        if form.is_valid():
            #Yes, save
            form.save()
            #redirect to home
            return HttpResponseRedirect ('/')
        else:    
            #No, show error
            return HttpResponseRedirect(form.erros.as_json())

    # Get all posts, limit = 20
    posts= Post.objects.all()[:20]

    # Show
    return render(request, 'posts.html',
                    {'posts': posts})  

def delete(request, post_id):
    # find post id 
    post = Post.objects.get(id=post_id)
    post.delete()
    return HttpResponseRedirect('/')

def edit(request, post_id):
     posts = Post.objects.get(id = post_id)
     if request.method == 'POST':
          form = PostForm(request.POST, request.FILES, instance=posts)
          if form.is_valid():
               form.save()
               return HttpResponseRedirect('/')
          else:
               return HttpResponseRedirect("not valid") 
     return render(request, 'edit.html',{'posts': posts})
  

