"""DjangoProject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.conf.urls import include
from myapp import views


urlpatterns = [
    # url(r'^$', views.homepage, name="home"),
    path('myapp/', include('myapp.urls')),
    path('django08/', include('django08.django08_url')),
    path('admin/', admin.site.urls),
    path('captcha/', include('captcha.urls')),

]

# handler404 = views.page_not_found
# handler500 = views.server_error
