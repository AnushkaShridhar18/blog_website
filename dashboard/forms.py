from django import forms 
from blogs.models import Category,Blogs
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User,Group

class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = '__all__'

class BlogPostForm(forms.ModelForm):
    class Meta:
        model = Blogs
        fields = ('title','category','blog_image','short_description','blog_body','status','is_featured')

class AddUserForm(UserCreationForm):
    email = forms.EmailField(required=True)  # Ensure email is required
    is_staff = forms.BooleanField(required=False)  # Checkbox for staff status
    is_superuser = forms.BooleanField(required=False)  # Checkbox for superuser status
    groups = forms.ModelMultipleChoiceField(
        queryset=Group.objects.all(),
        required=False,
        widget=forms.CheckboxSelectMultiple
    )  # Allow selecting groups

    class Meta:
        model = User
        fields = ('username', 'email', 'first_name', 'last_name', 'password1', 'password2', 'is_staff', 'is_superuser', 'groups')

    def save(self, commit=True):
        user = super().save(commit=False)

        # Handle passwords properly
        user.set_password(self.cleaned_data['password1'])

        # Handle superuser & staff status
        user.is_staff = self.cleaned_data['is_staff']
        user.is_superuser = self.cleaned_data['is_superuser']

        if commit:
            user.save()
            self.save_m2m()  # Save ManyToMany fields (like groups)
        return user
    
class EditUserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('username', 'email', 'first_name', 'last_name', 'is_staff', 'is_superuser', 'groups')