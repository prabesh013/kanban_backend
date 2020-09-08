from django.urls import path
from . import views


urlpatterns = [
    path("board/", views.BoardList.as_view()),
    path("board/<int:pk>", views.BoardList.as_view()),
    path("list/", views.ListList.as_view()),
    path("list/<int:pk>", views.ListList.as_view()),
    path("card/", views.CardList.as_view()),
    path("card/<int:pk>", views.CardList.as_view())
]
