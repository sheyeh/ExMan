from django.conf.urls import include, url
from django.contrib import admin

import expenses.views
import users.views

urlpatterns = [
    url(r'^$', expenses.views.HomeView.as_view(), name="home"),
    url(r'^add/$', expenses.views.AddView.as_view(), name="add"),
    url(r'^accounts/login/', users.views.CustomLoginView.as_view()),
    url(r'^accounts/', include('authtools.urls')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^add-account/', users.views.AddAccountView.as_view(), name="add-account"),
    url(r'^account/(?P<pk>[0-9]+)/$', users.views.OneAccountView.as_view(), name="account-details"),
    url(r'^account/$', users.views.AccountView.as_view(), name="account"),
]
