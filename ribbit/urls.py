"""ribbit URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
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
from django.conf.urls import url,include
from django.contrib import admin
from ribbit_app import views

from ribbit import settings

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', views.index), # root
    url(r'^login$', views.login_view), # login
    url(r'^logout$', views.logout_view), # logout
    url(r'^signup$', views.signup),
    url(r'^ribbits$', views.public), 
    url(r'^submit$', views.submit),
    url(r'^users/$', views.users),
    url(r'^users/(?P<username>\w{0,30})/$', views.users),
    url(r'^follow$', views.follow),
]
urlpatterns += patterns('',
        (r'^static/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.STATIC_ROOT}),
    )