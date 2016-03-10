"""trydjango18 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import include, url
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    url(r'^$', 'newsletter.views.home', name='home'),
    url(r'^(?P<num>[0-9]*)/$', 'newsletter.views.searchpage', name='searchpage'),
    url(r'^contact/$', 'newsletter.views.contact', name='contact'),
    url(r'^memberregister/(?P<num>[0-9]*)/(?P<num1>[0-9]*)$', 'newsletter.views.memberregister', name='memberregister'),
    url(r'^login/$', 'newsletter.views.sellerlogin', name='login'),
    url(r'^pclogin/$', 'newsletter.views.pclogin', name='pclogin'),
    url(r'^pclogin/pcview/$', 'newsletter.views.pcview', name='pcview'),
    url(r'^login/admin/\w+/(?P<num>[0-9]*)/$', 'newsletter.views.notify'),
    # url(r'^login/admin/\w+/(?P<num>[0-9]*)/Results/$', 'newsletter.views.results'),
    url(r'^login/(?P<username>\w+)/$', 'newsletter.views.userpage'),
    url(r'^login/(?P<username>\w+)/(?P<num>[0-9]*)/$', 'newsletter.views.edit'),
    url(r'^login/(?P<username>\w+)/config$', 'newsletter.views.config'),
    url(r'^login/(?P<username>\w+)/logout/$', 'newsletter.views.logout'),
    url(r'^login/admin/(?P<username>\w+)/$', 'newsletter.views.adminpage'),
    url(r'^search/$', 'newsletter.views.search', name='search'),
    url(r'^logout/$', 'newsletter.views.loggout'),
    url(r'^test1/$', 'newsletter.views.myview'),
    url(r'^login/admin/\w+/(?P<num>[0-9]*)/delete/$','newsletter.views.delete',name = 'delete'),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^accounts/', include('registration.backends.default.urls')),
    
]

if settings.DEBUG:
	urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
	urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)