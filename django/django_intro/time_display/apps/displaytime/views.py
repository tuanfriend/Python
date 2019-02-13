from django.shortcuts import render	# notice the import!
from time import gmtime, strftime

def index(request):
    context = {
        "time": strftime("%Y-%m-%d %H:%M %p", gmtime())
    }
    return render(request, "displaytime/index.html",context)