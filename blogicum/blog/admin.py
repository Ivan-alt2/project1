from django.contrib import admin
from blog.models import Post, Category, Location


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    search_fields = (
        'title',
        'text',
    )
    # pub_date — это DateTimeField, по нему search_fields обычно не делают:
    # поиск по дате делается через list_filter или date_hierarchy.
    list_display = ('title', 'author', 'pub_date', 'is_published')
    list_filter = ('is_published', 'category', 'location')
    date_hierarchy = 'pub_date'


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    search_fields = (
        'title',
        'description',
    )
    list_display = ('title', 'slug', 'is_published')


@admin.register(Location)
class LocationAdmin(admin.ModelAdmin):
    search_fields = ('name',)
    list_display = ('name', 'is_published')


admin.site.empty_value_display = 'Не задано'
