from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('memory_matching/', views.memory_matching, name='memory_matching'),
    path('tic_tac_toe/', views.tic_tac_toe, name='tic_tac_toe'),
    path('whack_a_mole/', views.whack_a_mole, name='whack_a_mole'),
    path('snake_game/', views.snake_game, name='snake_game'),
    path('puzzle_2048/', views.puzzle_2048, name='puzzle_2048'),
    path('rock_paper_scissors/', views.rock_paper_scissors, name='rock_paper_scissors'),
    path('hangman/', views.hangman, name='hangman'),
]
