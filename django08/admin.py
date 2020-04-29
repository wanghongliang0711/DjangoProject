from django.contrib import admin
from django08 import models

# Register your models here.
class PostAdmin(admin.ModelAdmin):
    list_display = ('id', 'mood', 'nickname', 'message', 'del_pass', 'enabled', 'pub_time')


class MoodAdmin(admin.ModelAdmin):
    list_display = ('id', 'status' )

admin.site.register(models.Mood, MoodAdmin)
admin.site.register(models.Post, PostAdmin)

