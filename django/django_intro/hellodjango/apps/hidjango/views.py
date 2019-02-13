# from django.shortcuts import render, HttpResponse, redirect
# def index(request):
#     return HttpResponse("placeholder to later display a list of all blogs")

# def new(request):
#     return HttpResponse("placeholder to display a new form to create a new blog")

# def create(request):
# 	return redirect("/")

# def show(request,id):
# 	return HttpResponse("placeholder to display blog number "+id)

# def editshow(request,id):
# 	return HttpResponse("placeholder to edit blog "+id)

# def destroy(request,id):
# 	return redirect("/")

from django.shortcuts import render
    
def index(request):
    context = {
    	"name": "Noelle",
    	"favorite_color": "turquoise",
    	"pets": ["Bruce", "Fitz", "Georgie"]
    }
    return render(request, "hidjango/index.html", context)
