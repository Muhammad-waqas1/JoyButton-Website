from django.shortcuts import render

def index(request):
    return render(request, 'game/index.html')

def memory_matching(request):
    return render(request, 'game/memory_matching.html')

def tic_tac_toe(request):
    return render(request, 'game/tic_tac_toe.html')

def whack_a_mole(request):
    return render(request, 'game/whack_a_mole.html')

def snake_game(request):
    return render(request, 'game/snake_game.html')

def puzzle_2048(request):
    return render(request, 'game/puzzle_2048.html')

def rock_paper_scissors(request):
    return render(request, 'game/rock_paper_scissors.html')

def hangman(request):
    return render(request, 'game/hangman.html')
