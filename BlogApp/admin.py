from django.contrib import admin
from .models import Author,Post , Category ,Comment

@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ('author','username','created',)
    fieldsets = (
        ('AUTHOR NAME', {
          'fields': ('username','author',)
        }),
        ('AUTHOR SETTINGS', {
          'fields': ('image','specialty',)
        }),)
    ordering = ('username',)

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('title','created')
    fieldsets = (
        ('TITLE SECTION', {
            'fields': (('title','image'),)
        }),
        ('BODY SECTION', {
            'fields': ('desc','body',)
        }),
        ('Author & Categories', {
            'fields': ('author','category'),
        }),)
    ordering = ('-created',)
    search_fields = ('title',)
    list_filter =('created','author','category',)

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name','created',)
    fieldsets = (
        ('CATEGORY SECTION', {
            'fields': ('name', 'image','color'),
        }),)
    ordering = ('created',)

@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('commentPost','created')
    fieldsets = (
        ('TITLE SECTION', {
            'fields': (('commentPost','user'), 'comment',)
        }),)
    ordering = ('-created',)
    list_filter =('commentPost','user','created',) 
