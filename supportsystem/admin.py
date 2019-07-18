from django.contrib import admin

# Register your models here.
from .models import Role, Company, Post, Comment, ExtendedUserProfile

admin.site.register(ExtendedUserProfile)
admin.site.register(Role)
admin.site.register(Company)
admin.site.register(Post)
admin.site.register(Comment)
