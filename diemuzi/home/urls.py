from django.urls import path

from home import views

app_name = 'home'

urlpatterns = [
    path('', views.Index.as_view(), name='index'),

    path('faq', views.Faq.as_view(), name='faq'),

    path('privacy', views.Privacy.as_view(), name='privacy')
]
