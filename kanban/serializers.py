from rest_framework import serializers
from .models import Board, List, Card


class CardSerializer(serializers.ModelSerializer):
    class Meta:
        model = Card
        fields = ('id', 'title', 'description', 'status')


class ListSerializer(serializers.ModelSerializer):
    card = CardSerializer()

    class Meta:
        model = List
        fields = ('id', 'list_name', 'list_desc', 'board', 'card')


class BoardSerializer(serializers.ModelSerializer):
    list_det = ListSerializer()

    class Meta:
        model = Board
        fields = ('id', 'board_name', 'board_desc', 'list_det')
