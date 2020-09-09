from django.urls import path
from . import views


urlpatterns = [
    path("list/", views.ListListCreate.as_view()),
    path("list/<int:pk>", views.ListDetail.as_view()),
    path("card/", views.CardListCreate.as_view()),
    path("card/<int:pk>", views.CardDetail.as_view()),
    path("board/", views.BoardListCreate.as_view()),
    path("board/<int:pk>", views.BoardDetail.as_view()),
]
