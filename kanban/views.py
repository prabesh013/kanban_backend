from django.shortcuts import render
from rest_framework import generics
from .models import Board, List, Card
from .serializers import BoardSerializer, ListSerializer, CardSerializer


# Create your views here.
class BoardList(generics.ListCreateAPIView):
    queryset = List.objects.all()
    serializer_class = BoardSerializer


class ListList(generics.ListCreateAPIView):
    queryset = List.objects.all()
    serializer_class = ListSerializer


class CardList(generics.ListCreateAPIView):
    queryset = Card.objects.all()
    serializer_class = CardSerializer
