from django.shortcuts import render, redirect
import random

def index(request):
    if 'money' not in request.session:
        request.session['activites'] = ""
        request.session['money'] = 0
    return render(request, "ninja_gold/index.html")

def process(request):
    temp = request.session['money']
    if request.POST['building'] == 'farm':
        request.session['money'] += random.randint(10, 20)
        request.session['activites'] += "Earned "+ str(request.session['money']-temp) +" from the Farm! \n"
    if request.POST['building'] == 'cave':
        request.session['money'] += random.randint(5, 10)
        request.session['activites'] += "Earned "+ str(request.session['money']-temp) +" from the Cave! \n"
    if request.POST['building'] == 'house':
        request.session['money'] += random.randint(2, 5)
        request.session['activites'] += "Earned "+ str(request.session['money']-temp) +" from the House! \n"
    if request.POST['building'] == 'casino':
        if (random.randint(1, 2)%2) == 0:
            request.session['money'] += random.randint(0, 50)
            request.session['activites'] += "You entered casino and win "+ str(request.session['money']-temp) +" from the Casino! \n"
        else:
            request.session['money'] -= random.randint(0, 50)
            request.session['activites'] += "You entered casino and lost "+ str(request.session['money']-temp) +" from the Casino! \n"
    return redirect('/')

def reset(request):
    request.session.clear()
    return redirect('/')