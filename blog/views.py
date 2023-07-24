from django.shortcuts import render,HttpResponse,redirect
from . models import Post,BlogComment
from django.contrib.auth.models import User
from django.contrib import messages

# Create your views here.

def index(request):
    allposts = Post.objects.all()
    param = {'allposts':allposts}
    return render (request,'blog/index.html',param)

def blogPost(request,slug):
    post = Post.objects.filter(slug = slug).first()#[0]
    comments = BlogComment.objects.filter(post = post , parent =None)
    replies =   BlogComment.objects.filter(post = post ).exclude(parent=None)
    repdict = {}
    for reply in replies:
        if reply.parent.S_no not in repdict.keys():
            repdict[reply.parent.S_no] = [reply]
        else:
            repdict[reply.parent.S_no].append(reply)

    param = {'post':post,'comments':comments ,'user':request.user,'replydict':repdict}
    return render (request,'blog/blogpost.html',param)


def handlecomment(request):
    if request.method == "POST":
        comment= request.POST.get('comments')
        user = request.user
        post_Sno = request.POST.get('post_sno')
        post = Post.objects.get(S_no = post_Sno)
        parent_sno = request.POST.get('parentSno')
        if parent_sno == "":
            comment = BlogComment(comments = comment , user = user ,post = post)
            comment.save()
            messages.success(request,'your comment has been posted successfully')
        else:
            parent = BlogComment.objects.get(S_no = parent_sno)
            comment = BlogComment(comments = comment , user = user ,post = post ,parent = parent)
            comment.save()
            messages.success(request,'your reply  has been posted successfully')



    return redirect(f"/blog/{post.slug}")



