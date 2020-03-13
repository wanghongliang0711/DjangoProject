from django.contrib import admin
from .models import Users
# Register your models here.


class UsersAdmin(admin.ModelAdmin):
    list_display = ('id', 'username', 'password', 'power')


admin.site.register(Users, UsersAdmin)
