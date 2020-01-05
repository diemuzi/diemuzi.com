from django.contrib.auth.views import LogoutView
from django.urls import path
from django.urls import re_path

from login import views

app_name = 'login'

urlpatterns = [
    path('', views.Index.as_view(redirect_authenticated_user=True), name='login'),

    re_path(r'^access'
            r'(?:/ipaddress/(?P<ipaddress>[\s\w -:]+))?'
            r'(?:/reverse_ipaddress/(?P<reverse_ipaddress>[\s\w -:]+))?'
            r'$',
            views.Access.as_view(), name='access'),

    path('create', views.Create.as_view(), name='create'),

    path('delete', views.Delete.as_view(), name='delete'),

    path('logout', LogoutView.as_view(), name='logout'),

    path('password', views.Password.as_view(), name='password'),

    path('profile', views.Profile.as_view(), name='profile')
]
