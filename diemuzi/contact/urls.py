from django.urls import path
from django.urls import re_path

from contact import views

app_name = 'contact'

urlpatterns = [
    path('', views.Index.as_view(), name='index'),

    path('delete/<int:pk>', views.Delete.as_view(), name='delete'),

    path('read/<int:pk>', views.Read.as_view(), name='read'),

    re_path(r'^search'
            r'(?:/name/(?P<name>[\s\w\'-]+))?'
            r'(?:/email/(?P<email>[\d\w.@-_]+))?'
            r'$',
            views.Search.as_view(), name='search')
]
