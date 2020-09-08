from django.db import models

# Create your models here.


class Board(models.Model):
    board_name = models.CharField(max_length=100)
    # created_by

    def __str__(self):
        return str(self.board_name)


class List(models.Model):
    list_name = models.CharField(max_length=100)
    board = models.ForeignKey(Board, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.list_name)


class Card(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    status = models.ForeignKey(List, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.title)
