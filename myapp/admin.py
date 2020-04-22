from django.contrib import admin
from .models import Users, Jsontable102
# Register your models here.


class UsersAdmin(admin.ModelAdmin):
    list_display = ('id', 'username', 'password', 'power', 'apply')

class Jsontable102Admin(admin.ModelAdmin):
    list_display = ('id', 'createdtime', 'fileno', 'metadata_positioning_data_positioning_time', 'metadata_positioning_data_quality')

admin.site.register(Users, UsersAdmin)
admin.site.register(Jsontable102, Jsontable102Admin)
