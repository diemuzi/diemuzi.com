from django.urls import path

from about import views

app_name = 'about'

urlpatterns = [
    path('', views.Index.as_view(), name='index')
]
