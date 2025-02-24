from django.shortcuts import redirect, render
from blogs.models import Blogs, Category
from.forms import RegistrationForm

def home(request):
    categories = Category.objects.all()
    featured_post = Blogs.objects.filter(is_featured = True, status = 1)
    posts = Blogs.objects.filter(is_featured = False, status = 1)
    print(posts)

    context = {
        'categories' : categories,
        'featured_post': featured_post,
        'posts':posts

    }
    return render(request, 'home.html',context)

#register
def register(request):
    if request.method == "POST":
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')  # Redirect after successful registration
    else:
        form = RegistrationForm()

    return render(request, 'register.html', {'form': form})


#login
def login(request):
    return render(request, 'login.html')