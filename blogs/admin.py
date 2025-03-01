from django.contrib import admin
from django.utils.html import format_html
from .models import Blogs, Category,Comment

class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'category_name', 'created_at', 'updated_at')
    search_fields = ('category_name',)

class BlogAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'category', 'author', 'image_preview', 'status', 'is_featured', 'created_at')
    list_filter = ('category', 'status')
    prepopulated_fields = {'slug': ('title',)}
    search_fields = ('id', 'title', 'category__category_name', 'status')
    list_editable = ('is_featured',)

    def image_preview(self, obj):
        """ Show image preview in the admin panel """
        if obj.blog_image:
            return format_html('<img src="{}" width="100" height="60" style="object-fit: cover;" />', obj.blog_image.url)
        return "(No Image)"
    
    image_preview.short_description = "Preview"

admin.site.register(Category, CategoryAdmin)
admin.site.register(Blogs, BlogAdmin)
admin.site.register(Comment)
