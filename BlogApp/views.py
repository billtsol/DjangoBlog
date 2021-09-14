from django.shortcuts import redirect, render
from .models import Post  ,Category ,Author,User ,Comment
from django.core.mail import send_mail
from .forms import ContactForm  ,RegisterForm ,LogInForm,CommentForm
from validate_email import validate_email
from django.core.paginator import Paginator
from django.contrib.auth import authenticate , login ,logout

footer =[
    {"title":"Features","urls": "#"},
    {"title":"Contact us","urls": "#"},
    {"title":"Get Theme","urls": "#"},
    {"title":"Support","urls": "#"},
    {"title":"News","urls": "#"},
    {"title":"Technology","urls": "#"},
    {"title":"Startups","urls": "#"},
    {"title":"Career","urls": "#"},
]
social = [
    {"title": "instagram","iclass": "fab fa-facebook-square fa-fw me-2 text-facebook","urls": 'https://www.instagram.com/'},
    {"title": "Twitter","iclass": "fab fa-twitter-square fa-fw me-2 text-twitter","urls": 'https://twitter.com/?lang=en'},
    {"title": "Youtube","iclass": "fab fa-youtube-square fa-fw me-2 text-youtube","urls":'https://www.youtube.com/'},
]

try:
    allPost = Post.objects.all().order_by('-created')
except:
    allPost = {}

try:
    categories = Category.objects.all()
except:
    categories = {}

try:
    authors = Author.objects.all()
except:
    authors={}

def Home(request):
    try:
        latestPost = Post.objects.order_by('-id')[0]
    except:
        latestPost=None
    try:
        lastOne = Post.objects.order_by('-id')[1]
    except:
        lastOne = None
    try:
        lastTwo = {Post.objects.order_by('-id')[2],Post.objects.order_by('-id')[3],}
    except:
        lastTwo= None
    page = 4


    content = {
        "latestPost":latestPost,
        "lastOne":lastOne,
        "lastTwo":lastTwo,
        "allPost": allPost,
        "page": page,
        "categories":categories,
        "footer":footer,
        "social":social,
    }
    return render(request, 'index.html' , content )

def AboutUs(request):
    content = {
        "authors":authors, 
        "categories":categories,
        "footer":footer,
        "social":social,
    }
    return render(request, 'about.html' , content )

def Contact(request):
    form = ContactForm()
    success = False
    if request.method =="POST":
        notValid = False
        emailName = request.POST['emailName']
        emailSubject =request.POST['emailSubject']
        email =request.POST['email']
        emailMessage = request.POST['emailMessage']
        message = 'SendBy: ' + email +'\n \n \
        User Name: ' + emailName + '\n \
        \n \n ' + emailMessage
        is_valid = validate_email(email)
        if is_valid:
            try:
                send_mail(
                    emailSubject,#Subject
                    message, #message
                    email,
                    ['billtsol2003@gmail.com'])
                success = True
            except:
                notValid = True
        else:
            notValid = True
        content = {
            "authors":authors, 
            "categories":categories,
            "footer":footer,
            "social":social,
            "form":form,
            "success":success,
            "notValid":notValid,
        }
        return render(request, 'contact.html',content)
    content = {
        "authors":authors, 
        "categories":categories,
        "footer":footer,
        "social":social,
        "form":form,
        "success":success,
    }
    return render(request, 'contact.html' , content )

def posts(request):
    allPosts = Post.objects.all().order_by('-created')
    paginator = Paginator(allPosts,2)
    page_number = request.GET.get('page')
    posts_obj = paginator.get_page(page_number)

    content = {
        "allPosts":posts_obj,
        "footer":footer,
        "social":social,
        "categories":categories,
    }
    return render(request, 'post.html' , content )

def postView(request,id):
    postDetail = Post.objects.get(id=id)
    PostBody = postDetail.body
    form = CommentForm()
    if request.method =="POST":
        message = request.POST.get('commentMessage')
        if request.user.is_authenticated:
            username = request.user.username
            Comment.objects.create(
                comment_post=postDetail,
                comment_user = username,
                comment_body=message,)
    content = {
        "form":form, 
        "postDetail":postDetail,
        "PostBody":PostBody,
        "footer":footer,
        "social":social,
        "categories":categories,
    }
    return render(request, 'postView.html' , content )

def categoryView(request,name):
    id = Category.objects.get(name=name).id
    allPosts = Post.objects.all().filter(category=id).order_by('-created')
    paginator = Paginator(allPosts,2)
    page_number = request.GET.get('page')
    posts_obj = paginator.get_page(page_number)
    content = {
        "posts":posts_obj,
        "categories":categories,
        "footer":footer,
        "social":social,
    }
    return render(request, 'category.html' , content )

def registerView(request):
    form = RegisterForm()
    notValid = False
    passwordnotsame = False
    success = False 
    isIn = False
    small = False
    if request.method =="POST":
        email = request.POST['email']
        usename = ''
        pos = 0
        for i in range(len(email)):
            if email[i]=="@":
                pos=i
        usename = email[0:pos]
        password1 =request.POST['password1']
        password2 =request.POST['password2']

        is_valid = validate_email(email)
        if is_valid:
            if password1==password2:
                if len(password1)<8:
                    small=True
                else:
                    userList = []
                    users = User.objects.all()
                    for user in users:
                        userList.append(user.email)
                    if email in userList:
                        isIn = True
                    else:
                        u = User(
                            email=email,
                            username=usename)    
                        u.set_password(password1)
            
                        u.save()
                        success = True
            else:
                passwordnotsame = True
        else:
            notValid = True
        if success:
            return redirect('Login')

    content = {
        "small":small,
        "passwordnotsame":passwordnotsame,
        "isIn":isIn,
        "success":success,
        "notValid":notValid,
        "form":form,
        "footer":footer,
        "social":social,
        "categories":categories,
    }
    return render(request, 'register.html' , content )

def logInView(request):
    form = LogInForm()
    notUser = False
    if request.method =="POST":
        email = request.POST.get('email')
        password = request.POST.get('password')

        username = ''
        if "@" not in email:
            username=email
        else:
            pos = 0
            for i in range(len(email)):
                if email[i]=="@":
                    pos=i
            username = email[0:pos]

        user = authenticate(request,username=username,password=password)
        if user is not None:
            login(request,user)
            return redirect('Home')
        else:
            notUser = True
    content = {
        "notUser":notUser,
        "form":form,
        "footer":footer,
        "social":social,
        "categories":categories,
    }
    return render(request, 'login.html' , content )

def logOutUser(request):
    logout(request)
    return redirect('Home')

def bad_request(request,exception):
    content={
        "categories":categories,
        "footer":footer,
        "social":social,
    }
    return render(request, '404.html' , content )

def permission_denied(request,exception):
    content={
        "categories":categories,
        "footer":footer,
        "social":social,
    }
    return render(request, '404.html' , content )

def page_not_found(request,exception):
    content={
        "categories":categories,
        "footer":footer,
        "social":social,
    }
    return render(request, '404.html' , content )

def server_error(exception):
    content={
        "categories":categories,
        "footer":footer,
        "social":social,
    }
    return render('404.html' , content )

def error(request):
    content={
        "categories":categories,
        "footer":footer,
        "social":social,
    }
    return render(request,'404.html' , content )