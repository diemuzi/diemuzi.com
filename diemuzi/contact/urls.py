from django.urls import path

from contact import views

app_name = 'contact'

urlpatterns = [
    path('', views.Index.as_view(), name='index')
]
