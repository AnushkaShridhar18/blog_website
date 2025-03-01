from django.db import models
from django.contrib.auth.models import User
from django.utils.text import slugify

# Category Model
class Category(models.Model):
    category_name = models.CharField(max_length=50, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name_plural = 'Categories'

    def __str__(self):
        return self.category_name 


STATUS_CHOICE = (
    (0, 'Draft'),
    (1, 'Publish')
)

# Blogs Model
class Blogs(models.Model):
    title = models.CharField(max_length=100, unique=True)
    slug = models.SlugField(unique=True, blank=True)  # Auto-generate slug if empty
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name="blogs")
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name="blogs")
    blog_image = models.ImageField(upload_to='uploads/%Y/%m/%d', blank=True, null=True)  # ✅ Fixed image field
    short_description = models.TextField(max_length=1000)
    blog_body = models.TextField(max_length=3000)
    status = models.IntegerField(choices=STATUS_CHOICE, default=0)
    is_featured = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name_plural = 'Blogs'

    def __str__(self):
        return self.title
    
    def save(self, *args, **kwargs):
        """ Auto-generate slug from title if not provided """
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)

class Comment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    blog = models.ForeignKey(Blogs, on_delete=models.CASCADE)
    comment = models.TextField(max_length=250)
    created_at = models.DateTimeField(auto_now_add= True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.comment