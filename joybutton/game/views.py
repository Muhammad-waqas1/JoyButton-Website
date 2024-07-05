from django.shortcuts import render

def index(request):
    return render(request, 'index.html')

def memory_matching(request):
    return render(request, 'memory_matching.html')

def tic_tac_toe(request):
    return render(request, 'tic_tac_toe.html')

def whack_a_mole(request):
    return render(request, 'whack_a_mole.html')

def snake_game(request):
    return render(request, 'snake_game.html')

def puzzle_2048(request):
    return render(request, 'puzzle_2048.html')

def rock_paper_scissors(request):
    return render(request, 'rock_paper_scissors.html')

def hangman(request):
    return render(request, 'hangman.html')
