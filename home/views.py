from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect

from home.models import Post
# Create your views here.
def index(request):
    post_list = Post.objects.all().order_by("-pk")
    context = {
        "post_list": post_list
    }
    return render(request, "home/index.html", context)


def create_post(request):
    if request.method == "GET":
        return render(request, "home/create.html")
    elif request.method == "POST":
        new_post = Post()
        new_post.title = request.POST["title"]
        new_post.price = request.POST["price"]
        if request.FILES["image"]:
            new_post.image = request.FILES["image"]
        new_post.content = request.POST["content"]
        new_post.save()
        return HttpResponseRedirect("/")
        # return redirect("market:home")


def view_post(request, post_id):
    post = Post.objects.get(id=post_id)
    context = {
        "post": post,
    }
    return render(request, "home/post.html", context)


def update_post(request, post_id):
    if request.method == "GET":
        post = Post.objects.get(pk=post_id)
        context = {
            "post": post
        }
        return render(request, "home/update.html", context)
    elif request.method == "POST":
        post = Post.objects.get(pk=post_id)
        post.title = request.POST["title"]
        post.price = request.POST["price"]
        if request.FILES.get('image', False):
            post.image = request.FILES["image"]
        post.content = request.POST["content"]
        post.save()
        return HttpResponseRedirect(f"/view/{post_id}/")


def delete_post(request, post_id):
    target_post = Post.objects.get(pk=post_id)
    target_post.delete()
    return HttpResponseRedirect("/")