"""
URL configuration for app project.

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
from django.urls import path
from .views import Main

urlpatterns = [
    path('', Main.as_view())
]
""" 
여기서 Main옆에 붙은 as_view()는 클래스형 view(class Main을 의미)로 진입하기 위한 진입 메서드로 이해하면 됨,
class Main이 html을 rendering하기 위한 함수인데, 이 "함수로 진입하기 위해 사용하는 진입메서드" 이다

메인 URL을 호출하면 Main.as_view()를 타고 view.html을 rendering하게 되겠지?
"""