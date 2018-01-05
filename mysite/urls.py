"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
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
from django.conf.urls import url
from django.contrib import admin
from learn import views as learn_views
from calc import views as calc_views
from tools import views as tools_views

urlpatterns = [
    url(r'^send_email/', tools_views.send_email, name='send_email'),
    url(r'^new_add/(\d+)/(\d+)/$', calc_views.add2, name='add2'),
    url(r'^add/(\d+)/(\d+)/$', calc_views.old_add2_redirect),
    url(r'^add/$', calc_views.add, name='add'),
    url(r'^$', tools_views.index, name='home'),
    url(r'^admin/', admin.site.urls),
]
