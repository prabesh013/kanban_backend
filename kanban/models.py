from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Board(models.Model):
    board_name = models.CharField(max_length=100)
    board_desc = models.CharField(max_length=200)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.board_name)


class List(models.Model):
    list_name = models.CharField(max_length=100)
    list_desc = models.CharField(max_length=200)
    board = models.ForeignKey(Board, on_delete=models.CASCADE)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.list_name)


class Card(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    status = models.ForeignKey(List, on_delete=models.CASCADE)
    board_status = models.ForeignKey(Board, on_delete=models.CASCADE)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.title)
