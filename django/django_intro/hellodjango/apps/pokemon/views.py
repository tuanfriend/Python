from django.shortcuts import render, redirect

def index(request):
    board =""
    for i in range(1,152):
        board += "<img src='https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/shiny/"+str(i)+".png'>"
    context = {
        "board": board
    }
    return render(request, "pokemon/index.html", context)