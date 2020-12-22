"""project URL Configuration

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
from django.urls import path, re_path
from django.conf.urls import url, include
from web_app import page

urlpatterns = [
    re_path(r'^$', page.index),
    re_path(r'^top', page.top),
    re_path(r'^menu', page.menu),
    re_path(r'^default', page.default),
    path("status_page/", page.status_page),
    re_path('status_page/fetch/', page.fetch),
    path("singleLine_page/", page.singleLine_page),
    re_path('singleLine_page/search/', page.search),
    path("compare_page/", page.compare_page),
    re_path('compare_page/compare/', page.compare),
    path("report_page/", page.report_page),
    re_path('report_page/report/', page.report),
    re_path('report_page/create_img/', page.create_img),
    re_path('report_page/search/', page.search),
    re_path('report_page/download_report/', page.download_report),
    re_path('report_page/download_template/', page.download_template),
    re_path('report_page/clear_session/', page.clear_session),
    path("email_page/", page.email_page),
    re_path('email_page/send_email/', page.send_email),

]
