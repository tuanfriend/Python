from django.shortcuts import render
from .models import User

def index(request):
    context = {
    	"all_user": User.objects.all()
    }
    return render(request, "users_app/index.html", context)

