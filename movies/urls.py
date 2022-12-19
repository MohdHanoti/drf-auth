from django.urls import path
from .views import MoviesListCreateView,MoviesDetailView
urlpatterns = [
    path('',MoviesListCreateView.as_view(),name='movies_list_create'),
    path('<int:pk>',MoviesDetailView.as_view(),name='movies_detail'),

    
]