from django.db import models

# Create your models here.


class Users(models.Model):
    username = models.CharField(max_length=20)
    password = models.CharField(max_length=20)
    power = models.IntegerField(default=1)  # 0 是管理员 1 是普通用户
    apply = models.IntegerField(default=1)  # 0 不可用 1 可用

    def __unicode__(self):
        return self.username
