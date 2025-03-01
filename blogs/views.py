from django.shortcuts import render, redirect, get_object_or_404
from django.db.models import Q
from .models import Blogs, Category,Comment
from blog_main.forms import RegistrationForm  # ✅ Import from blog_main
from django.contrib.auth.forms import AuthenticationForm
from django.contrib import auth
from django.http import HttpResponseRedirect

def home(request):
    categories = Category.objects.all()
    featured_post = Blogs.objects.filter(status=1, is_featured=True)
    posts = Blogs.objects.filter(status=1, is_featured=False)

    context = {
        'categories': categories,
        'featured_post': featured_post,
        'posts': posts,
    }
    return render(request, 'home.html', context)

def posts_by_category(request, category_id):
    category = get_object_or_404(Category, id=category_id)
    posts = Blogs.objects.filter(status=1, category=category)
    categories = Category.objects.all()

    context = {
        'category': category,
        'posts': posts,
        'categories': categories,
    }
    return render(request, 'posts_by_category.html', context)

#blogs
def blogs(request, slug):
    blog = get_object_or_404(Blogs, slug=slug, status=1)
    #comment
    comment = Comment()
    if request.method == "POST":
        comment.user = request.user
        comment.blog = blog
        comment.comment = request.POST['comment']
        comment.save()
        return HttpResponseRedirect(request.path_info)
    comments = Comment.objects.filter(blog = blog)
    comment_count = comments.count()
    context = {
        'blog' :  blog,
        'comments' : comments,
        'comments_count':comment_count

    }
    return render(request,'blogs.html',context)
    
   

def search(request):
    keyword = request.GET.get('keyword')
    blogs = Blogs.objects.filter(Q(title__icontains=keyword) | Q(short_description__icontains=keyword), status=1)

    context = {
        'blogs': blogs,
        'keyword': keyword,
    }
    return render(request, 'search.html', context)

def register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')  # Redirect to home after successful registration
    else:
        form = RegistrationForm()
    
    context = {'form': form}
    return render(request, 'register.html', context)

#login
def login(request):
    if request.method == "POST":
        form = AuthenticationForm(request, request.POST)

        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']

            user = auth.authenticate(username = username,password = password)
            if user is not None:
                auth.login(request,user)
                return redirect('dashboard')

    else:

        form = AuthenticationForm()
    context = {
        'form': form
    }
    return render(request, 'login.html',context)

#Logout

def logout(request):
    auth.logout(request)
    return redirect('home')
