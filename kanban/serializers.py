from rest_framework import serializers
from .models import Board, List, Card


class CardSerializer(serializers.ModelSerializer):
    created_by = serializers.ReadOnlyField(source='created_by.username')

    class Meta:
        model = Card
        fields = ('id', 'title', 'description',
                  'status', 'board_status', 'created_by')


class ListSerializer(serializers.ModelSerializer):
    # cards = CardSerializer(many=True, read_only=True)
    created_by = serializers.ReadOnlyField(source='created_by.username')

    class Meta:
        model = List
        fields = ('id', 'list_name', 'list_desc', 'board', 'created_by')


class BoardSerializer(serializers.ModelSerializer):
    # list_det = ListSerializer(many=True, read_only=True)
    created_by = serializers.ReadOnlyField(source='created_by.username')

    class Meta:
        model = Board
        fields = ('id', 'board_name', 'board_desc', 'created_by')
