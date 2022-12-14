"""headmanager URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from django.urls import path, include
from rest_framework.routers import SimpleRouter
from django.contrib.auth import views as auth_views

from hrmanager.views import VacancyViewSet, index, login_test, CandidateViewSet

router = SimpleRouter()
router.register('api/vacancys', VacancyViewSet)
router.register('api/candidats', CandidateViewSet)

urlpatterns = [
    path('', index),
    path('admin/', admin.site.urls),
    path('ll/', login_test),
    path('accounts/login/', auth_views.LoginView.as_view(template_name='login.html'), name="login"),
    path('api/', include('hrmanager.urls')),
    path('api/drf-auth/', include('rest_framework.urls'))
]

urlpatterns += router.urls
