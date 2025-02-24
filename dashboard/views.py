from .forms import CategoryForm
from django.shortcuts import get_object_or_404, render,redirect
from blogs.models import Category,Blogs
from django.contrib.auth.decorators import login_required

@login_required(login_url='login')
def dashboard(request):
    category_count = Category.objects.all().count()
    blogs_count = Blogs.objects.all().count()
    context = {
        'category_counts' : category_count,
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