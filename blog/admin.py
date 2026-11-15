from django.contrib import admin

from .models import Category, Comment, Post


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'description')


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'posted_at')
    filter_horizontal = ('categories',)


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('post', 'author', 'posted_at')
