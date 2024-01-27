from django.contrib import admin
from .models import Post, Category

# Register your models here.
class CategoryAdmin(admin.ModelAdmin):
    readonly_fields=('created', 'updated')  # Para que no se pueda editar en el admin

class PostAdmin(admin.ModelAdmin):
    readonly_fields=('created', 'updated')  # Para que no se pueda editar en el admin    
    list_display=('title', 'author', 'published')  # Para que se muestre en el 
    ordering=('author', 'published')  # Para que se muestre en el
    search_fields=('title', 'content', 'author__username', 'categories__name')  # Para que se muestre en el
    list_filter=('author__username', 'categories__name')  # Para que se muestre en el

    def post_categories(self, obj):
        return ", ".join([c.name for c in obj.categories.all().order_by("name")])   
    post_categories.short_description="Categorias"  # Para que se muestre en el

admin.site.register(Category, CategoryAdmin)
admin.site.register(Post, PostAdmin)