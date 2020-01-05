from django.urls import path

from photo import views

app_name = 'photo'

urlpatterns = [
    path('', views.Index.as_view(), name='index')
]
