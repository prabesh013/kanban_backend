from django.shortcuts import render
from rest_framework import generics
from .models import Board, List, Card
from .serializers import BoardSerializer, ListSerializer, CardSerializer


# Create your views here.
class BoardListCreate(generics.ListCreateAPIView):
    queryset = Board.objects.all()
    serializer_class = BoardSerializer


class BoardDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Board.objects.all()
    serializer_class = BoardSerializer


class ListListCreate(generics.ListCreateAPIView):
    queryset = List.objects.all()
    serializer_class = ListSerializer


class ListDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = List.objects.all()
    serializer_class = ListSerializer


class CardListCreate(generics.ListCreateAPIView):
    queryset = Card.objects.all()
    serializer_class = CardSerializer


class CardDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Card.objects.all()
    serializer_class = CardSerializer
