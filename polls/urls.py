from django.urls import path

from . import views

app_name = 'polls'  # Allows django to differentiate urls names between apps
urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('<int:pk>/', views.DetailView.as_view(), name='detail'),
    path('<int:pk>/result/', views.ResultsView.as_view(), name='results'),
    path('<int:question_id>/vote/', views.vote, name='vote'),
]


# Path function has different arguments
# Path route - string containing url pattern
# Path view - binds certain view to the url
# Path kwarg - Arbitrary keyword arguments can be passed in a dictionary to the target view
# Path name - Naming your URL lets you refer to it unambiguously from elsewhere in Django, especially from within templates. 
# This powerful feature allows you to make global changes to the URL patterns of your project while only touching a single file.