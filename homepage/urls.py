from django.urls import path

from . import views

app_name = 'polls'  # Allows django to differentiate urls names between apps
urlpatterns = [
    path('', views.homepage, name='index'),
]