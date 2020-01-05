from django.urls import path

from member import views

app_name = 'member'

urlpatterns = [
    path('', views.Index.as_view(), name='index')
]
