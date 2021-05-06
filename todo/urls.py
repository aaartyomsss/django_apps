from django.urls import path

from . import views

app_name = 'todo'  # Allows django to differentiate urls names between apps
urlpatterns = [
    path('', views.home, name='index'),
    path('registration/', views.registration, name='registration'),

]