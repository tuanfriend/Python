from django.shortcuts import render, redirect
from django.utils.crypto import get_random_string

def index(request):
    if 'count' not in request.session:
        request.session['count'] = 0
    else:
        request.session['count'] += 1
    context = {
    "text": get_random_string(length=14)
    }
    return render(request, "random_word/index.html",context)

def reset(request):
    request.session.clear()
    return redirect('/')
# def count(request):
#     if request.method == "POST":
#         request.session['count'] += 1
#     return render(request, "random_word/index.html")

# def random_word(request):
#     context = {
#         "text": get_random_string(length=14)
#         }
#     return render(request, "random_word/index.html", )
