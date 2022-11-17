from django.urls import path 
from .views import *

urlpatterns = [
    path("new", CreateGameAPI.as_view(), name="create_new_game"),
    path("<int:id>", GetGameStateAPI.as_view(), name="get_game_state"),
    path("<int:id>/guess", UpdateGameState.as_view(), name="update_game_state"),
]