"""sample_project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin
from django.views.generic.base import RedirectView
from django.contrib.auth import views as auth_views


urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^auth/', include('gcb_web_auth.urls')),
    url(r'^accounts/login/$', auth_views.login, {'template_name': 'gcb_web_auth/login.html'}, name='login'),
    url(r'^accounts/logout/$', auth_views.logout, {'template_name': 'gcb_web_auth/logged_out.html'}, name='logout'),
    url(r'^accounts/login-local/$', auth_views.login, {'template_name': 'gcb_web_auth/login-local.html'},
        name='login-local'),
    # Redirect / to /accounts/login
    url(r'^$', RedirectView.as_view(pattern_name='auth-home', permanent=False)),

]
