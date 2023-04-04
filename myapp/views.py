from django.shortcuts import render

# Create your views here.
def city(request):
    return render(request, "myapp/city.html")

def area_roles(request):
    return render(request, "myapp/area-roles.html")

def social_auth(request):
    return render(request, "myapp/social-auth.html")

def signup(request):
    return render(request, "myapp/signup.html")