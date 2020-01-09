from django.urls import path
from django.urls import re_path

from photo import views

app_name = 'photo'

urlpatterns = [
    path('admin/add', views.AdminAdd.as_view(), name='admin-add'),

    path('admin/add/album', views.AdminAddAlbum.as_view(), name='admin-add-album'),

    path('admin/delete/<int:pk>', views.AdminDelete.as_view(), name='admin-delete'),

    path('admin/delete/album/<int:pk>', views.AdminDeleteAlbum.as_view(), name='admin-delete-album'),

    path('admin/profile/<int:pk>', views.AdminProfile.as_view(), name='admin-profile'),

    re_path(r'^admin/search'
            r'(?:/name/(?P<name>[\s\w\'-]+))?'
            r'(?:/album/(?P<album>[\d]+))?'
            r'$',
            views.AdminSearch.as_view(), name='admin-search'),

    re_path(r'^admin/search/album'
            r'(?:/name/(?P<name>[\s\w\'-]+))?'
            r'$',
            views.AdminSearchAlbum.as_view(), name='admin-search-album'),

    re_path(r'^search'
            r'(?:/name/(?P<name>[\s\w\'-]+))?'
            r'(?:/album/(?P<album>[\d\s\w\'-]+))?'
            r'$',
            views.Search.as_view(), name='search'),

    path('', views.Index.as_view(), name='index')
]
