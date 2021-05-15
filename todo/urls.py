from django.urls import path

from . import views

app_name = 'todo'  # Allows django to differentiate urls names between apps
urlpatterns = [
    path('', views.home, name='index'),
    path('registration/', views.registration_req, name='registration'),
    path('login/', views.login_req, name='login'),
    path('logout/', views.logout_req, name='logout')
]