from django.shortcuts import render
from rest_framework.generics import ListCreateAPIView,RetrieveUpdateDestroyAPIView
# Create your views here.
from .models import Movies
from .serializers import MoviesSerializer
from .permissions import OwnerOnly

class MoviesListCreateView(ListCreateAPIView):
    
    queryset=Movies.objects.all()
    serializer_class=MoviesSerializer


class MoviesDetailView(RetrieveUpdateDestroyAPIView):
    queryset=Movies.objects.all()
    serializer_class=MoviesSerializer
    permission_classes=[OwnerOnly]