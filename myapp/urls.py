from django.urls import path
from myapp import views
from django.conf.urls import include

app_name = 'myapp'

user_patterns = [
    path('', views.userhomepage, name="userhomepage"),

]

urlpatterns = [
    path('', views.homepage, name="home"),
    path('login/', views.login, name="login"),
    path('registerpage/', views.registerpage, name="registerpage"),
    path('register/', views.register, name="register"),
    path('user/', include(user_patterns)),


]
