from django.urls import path
from django.urls import re_path

from blog import views

app_name = 'blog'

urlpatterns = [
    path('admin/add', views.AdminAdd.as_view(), name='admin-add'),

    path('admin/add/category', views.AdminAddCategory.as_view(), name='admin-add-category'),

    path('admin/delete/<int:pk>', views.AdminDelete.as_view(), name='admin-delete'),

    path('admin/delete/category/<int:pk>', views.AdminDeleteCategory.as_view(), name='admin-delete-category'),

    path('admin/profile/<int:pk>', views.AdminProfile.as_view(), name='admin-profile'),

    re_path(r'^admin/search'
            r'(?:/name/(?P<name>[\s\w\'-]+))?'
            r'(?:/category/(?P<category>[\d]+))?'
            r'$',
            views.AdminSearch.as_view(), name='admin-search'),

    re_path(r'^admin/search/category'
            r'(?:/name/(?P<name>[\s\w\'-]+))?'
            r'$',
            views.AdminSearchCategory.as_view(), name='admin-search-category'),

    re_path(r'^search'
            r'(?:/name/(?P<name>[\s\w\'-]+))?'
            r'(?:/category/(?P<category>[\d\s\w\'-]+))?'
            r'(?:/keyword/(?P<keyword>[-\w]+))?'
            r'$',
            views.Search.as_view(), name='search'),

    path('', views.Index.as_view(), name='index'),

    path('<int:pk>', views.Read.as_view(), name='read'),
    path('<slug:slug>', views.Read.as_view(), name='read'),
]
