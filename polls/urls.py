from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index')
]
# Path function has different arguments
# Path route - string containing url pattern
# Path view - binds certain view to the url
# Path kwarg - Arbitrary keyword arguments can be passed in a dictionary to the target view
# Path name - Naming your URL lets you refer to it unambiguously from elsewhere in Django, especially from within templates. 
# This powerful feature allows you to make global changes to the URL patterns of your project while only touching a single file.