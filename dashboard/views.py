from .forms import CategoryForm,BlogPostForm
from django.shortcuts import get_object_or_404, render,redirect
from blogs.models import Category,Blogs
from django.contrib.auth.decorators import login_required
from django.utils.text import slugify
from django.contrib.auth.models import User
from .forms import AddUserForm,EditUserForm

@login_required(login_url='login') 
def dashboard(request):
    category_count = Category.objects.all().count()
    blogs_count = Blogs.objects.all().count()
    context = {
        'category_count' : category_count,
        'blog_count' : blogs_count
    }
    
    return render(request, 'dashboard/dashboard.html',context )  # Ensure this template exists

def categories(request):
    return render(request,'dashboard/categories.html')

def add_categories(request):
    if request.method == "POST":
        form = CategoryForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('categories')
        
    form = CategoryForm()
    context = {
        'form' : form
    }
    return render(request,'dashboard/add_categories.html',context)


def edit_categories(request, pk):
    category = get_object_or_404(Category, pk=pk)  
    if request.method == "POST":
        form = CategoryForm(request.POST,instance=category)
        if form.is_valid():
            form.save()
            return redirect('categories')
    form = CategoryForm(instance=category)
    context = {
        'form': form,
        'category': category  
    }
    return render(request, 'dashboard/edit_categories.html', context)


def delete_categories(request, pk):
    category = get_object_or_404(Category,pk=pk)
    category.delete()
    return redirect('categories')


def posts(request):
    posts = Blogs.objects.all()
    context ={
        'posts' : posts
    }
    return render(request,'dashboard/posts.html',context)

def add_posts(request):
    if request.method == "POST":
        form = BlogPostForm(request.POST, request.FILES)
        if form.is_valid():
            posts = form.save(commit=False)
            posts.author = request.user
            title = form.cleaned_data['title']  # ✅ Corrected
            posts.slug = slugify(title)  # ✅ Corrected
            posts.save()  # ✅ Corrected
            print("Success")
            return redirect('posts')
        else:
            print(form.errors)  # ✅ Debugging form errors

    form = BlogPostForm()
    context = {'form': form}
    return render(request, 'dashboard/add_posts.html', context)


def delete_posts(request,pk):
    posts = get_object_or_404(Blogs,pk=pk)
    posts.delete()
    return redirect('posts')


def users(request):
    users = User.objects.all()
    context ={
        'users':users
    }
    return render(request, 'dashboard/users.html',context)

def add_users(request):
    if request.method == "POST":
        form = AddUserForm(request.POST)
        if form.is_valid():
            user = form.save()  # Calls the save() method in AddUserForm
            return redirect('users')  # Redirect to user list page
        
        else:
            print(form.errors)  # Debugging: Print form errors

    else:
        form = AddUserForm()

    context = {'form': form}
    return render(request, 'dashboard/add_users.html', context)

def edit_user(request, pk):
    user = get_object_or_404(User, pk=pk)
    if request.method == "POST":
        form = EditUserForm(request.POST, instance=user)
        if form.is_valid():
            form.save()
            return redirect('users')  # Redirect to users list after update
    else:
        form = EditUserForm(instance=user)

    context = {'form': form, 'user': user}
    return render(request, 'dashboard/edit_users.html', context)

def delete_user(request,pk):
    user = get_object_or_404(User,pk=pk)
    user.delete()
    return redirect('users')