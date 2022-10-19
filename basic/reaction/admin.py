from dataclasses import fields
from pyexpat import model
from django.contrib import admin
from reaction.models import postData
# Register your models here.

class PostReaction(admin.ModelAdmin):
    class Meta:
        model = postData
admin.site.register(postData)
