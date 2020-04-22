from django.urls import path
from myapp import views
from django.conf.urls import include
from myapp.view.BaseView import BaseView
from myapp.views import Jsontable102List


app_name = 'myapp'


user_patterns = [
    path('', views.userhomepage, name="userhomepage"),

]

urlpatterns = [
    path('', views.homepage, name="home"),
    path('handlenmea/', views.handlenmea, name="handlenmea"),
    path('handlejson/', views.handlejson, name="handlejson"),

    path('test', views.test, name='test'),
    path('show13', views.Show13),
    path('testjs102/',Jsontable102List.as_view(),name='testjs102'),

    path('login/', views.login, name="login"),
    path('registerpage/', views.registerpage, name="registerpage"),
    path('register/', views.register, name="register"),
    path('line_basic/', views.line_basic, name="line_basic"),
    path('datatable_basic/', views.datatable_basic, name="datatable_basic"),
    path('line_basic_xAxis/', views.line_basic_xAxis, name="line_basic_xAxis"),
    path('user/', include(user_patterns)),


]
