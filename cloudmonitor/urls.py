"""cloudmonitor URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
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
from django.conf import settings
from django.conf.urls.static import static
from users import views
from admins import views as admv
from clouds import views as clv
from cloudmonitor import views as cmv
# from users.views import index,userlogin,adminlogin,cloudlogin,userregister,storeregistration,logout,userlogincheck,usercreateapp,appcreaterequest,useruploadfile,snippet_detail
# from admins.views import adminlogincheck,adminactivateusers,activatewaitedusers
# from clouds.views import activateuserapp,cloudlogincheck,clouduserappactivations
# from .views import resturl,downloadfile,deletefile,uploadfile

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.index,name='index'),
    path('accounts', views.AccountAPIView.as_view(), name='account-list'),
    path('contacts', views.ContactAPIView.as_view(), name='contact-list'),
    path('activities', views.ActivityAPIView.as_view(), name='activity-list'),
    path('activitystatuses', views.ActivityStatusAPIView.as_view(), name='activity-status-list'),
    path('contactsources', views.ContactSourceAPIView.as_view(), name='contact-source-list'),
    path('contactstatuses', views.ContactStatusAPIView.as_view(), name='contact-status-list'),
    path('logout',views.logout,name='logout'),

    path('adminlogincheck',admv.adminlogincheck,name='adminlogincheck'),
    path('adminactivateusers',admv.adminactivateusers,name='adminactivateusers'),
    path('activatewaitedusers/<id>/$',admv.activatewaitedusers,name='activatewaitedusers'),

    path('userlogin',views.userlogin,name='userlogin'),
    path('adminlogin', views.adminlogin, name='adminlogin'),
    path('cloudlogin', views.cloudlogin, name='cloudlogin'),
    path('userregister', views.userregister, name='userregister'),
    path('storeregistration',views.storeregistration,name='storeregistration'),
    path('userlogincheck', views.userlogincheck, name='userlogincheck'),
    path('usercreateapp',views.usercreateapp,name='usercreateapp'),
    path('appcreaterequest',views.appcreaterequest,name='appcreaterequest'),
    path('useruploadfile/<appname>/$',views.useruploadfile,name='useruploadfile'),
    path('^snippet_detail/$',views.snippet_detail,name='snippet_detail'),

    path('resturl/<id>',cmv.resturl,name='resturl'),
    path('downloadfile/<id>',cmv.downloadfile,name='downloadfile'),
    path('deletefile/<id>',cmv.deletefile,name='deletefile'),
    path('uploadfile',cmv.uploadfile,name='uploadfile'),


    path('activateuserapp',clv.activateuserapp,name='activateuserapp'),
    path('cloudlogincheck',clv.cloudlogincheck,name='cloudlogincheck'),
    path('clouduserappactivations/<appname>/$',clv.clouduserappactivations, name='clouduserappactivations'),



]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)