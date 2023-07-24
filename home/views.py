from django.shortcuts import render,HttpResponse,redirect
from  django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from home.models import Contact
from blog.models import Post

from django.contrib import messages

# Create your views here.
def index(request):
    return render (request,'home/index.html')

def contact(request):
    if request.method == 'POST':
        name = request.POST.get('name', '')
        email = request.POST.get('email', '')
        phone = request.POST.get('phone', '')
        desc = request.POST.get('desc', '')
        if len(name)<2 or len(email)<3 or len(phone)<10 or len(desc)<4:
             messages.error(request, "Please enter your correct information!.")
        else:
            contact = Contact(name = name, email = email, phone=phone,desc = desc)
            contact.save()
            messages.success(request, "Your from has been done.")

            
    return  render (request,'home/contact.html')

def about(request):
    return  render (request,'home/about.html')


def searchMatch(query, item):
    '''return true only if query matches the item'''
    if query in item.desc.lower() or query in item.title.lower() or query in item.author.lower():
        return True
    else:
        return False


def search(request):
    query = request.POST.get('search')
    if len(query)>50:
        allposts = Post.objects.none()# it's mean allposts is empty or allpost[]
    else:
        posttitle = Post.objects.filter(title__icontains = query)
        postdesc = Post.objects.filter(desc__icontains = query)
        postauthor = Post.objects.filter(author__icontains = query)
        allposts = posttitle.union(postdesc,postauthor)
    if allposts.count()==0:
        messages.warning(request, "Please enter relevent search information!.")
    param = {'allposts': allposts ,'query':query}  
    return render(request , 'home/search.html',param)

def handlesignup(request):
    if request.method == 'POST':
        username = request.POST.get('name',"")
        email = request.POST.get('email',"")
        fname = request.POST.get('fname',"")
        lname = request.POST.get('lname',"")
        pass1 = request.POST.get('password1',"")
        pass2 = request.POST.get('password2',"")
        #some check
        if len(username)>15:
            messages.error(request, "Please enter your name under the 15 character!.")
            return redirect('/') # redirect('/') same


        if pass1 != pass2:
            messages.error(request, "Your password does not match Pealse try again!.")
            return redirect('/') # redirect('/') same

       
        #create the user

        myuser =  User.objects.create_user(username,email,pass1)
        myuser.first_name = fname
        myuser.last_name = lname
        myuser.save()
        messages.success(request, "Your icoder account has been successfully created")
        return redirect('/') # redirect('/') same
    else:
        return HttpResponse("found error")


def handlerlogin(request): 
    if  request.method == "POST":
        name = request.POST.get('name1',"")
        password = request.POST.get('pass',"")
        user = authenticate(username = name , password = password)
        if user is not None:
            login(request,user)
            messages.success(request, "successfully logged in....")
            return redirect('/') 
        else:
             messages.error(request, "Invalid credentials .")
    return HttpResponse('404 not found')


def handlerlogout(request):
    logout(request)
    messages.success(request, "successfully logged out....")
    return redirect('/') 








   
