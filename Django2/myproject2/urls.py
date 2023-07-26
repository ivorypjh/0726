"""
URL configuration for myproject2 project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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

# 애플리케이션의 views.py 파일을 사용할 수 있도록 import
from myweb import views

# 사용할 url과 그를 처리할 방법을 지정
# "" 는 localhost:8000 을 처리
urlpatterns = [
    path("admin/", admin.site.urls),
    # myweb 애플리케이션의 views 파일 내의 index 함수가 처리
    path("", views.index),
    # localhost:8000/testhtml/ 요청이 오면
    # views 파일의 testhtml 함수가 처리
    path("testhtml/", views.testhtml),
    path("template/", views.template)
]
