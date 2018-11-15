from django.shortcuts import render, HttpResponse

# Create your views here.
def home(request):
    # return HttpResponse("<h1>Portada</h1>")
    return render(request,"core/home.html")
def about(request):
    # return HttpResponse("<h1>About</h1>")
    return render(request,"core/about.html")
def store(request):
    # return HttpResponse("<h1>Store</h1>")
    return render(request,"core/store.html")