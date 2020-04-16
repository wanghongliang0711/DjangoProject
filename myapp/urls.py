from django.urls import path
from myapp import views
from django.conf.urls import include
from myapp.view.BaseView import BaseView
app_name = 'myapp'


user_patterns = [
    path('', BaseView.userhomepage, name="userhomepage"),

]

urlpatterns = [
    path('', BaseView.homepage, name="home"),
    path('login/', BaseView.login, name="login"),
    path('registerpage/', views.registerpage, name="registerpage"),
    path('register/', views.register, name="register"),
    path('line_basic/', views.line_basic, name="line_basic"),
    path('line_basic_xAxis/', views.line_basic_xAxis, name="line_basic_xAxis"),
    path('user/', include(user_patterns)),


]
