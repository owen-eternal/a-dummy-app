# from django.urls import path
# from . import views
from django.urls import path
from . import views

urlpatterns = [
    path("candidate/city", views.city),
    path("candidate/area-roles", views.area_roles),
    path("candidate/signup", views.signup),
    path("candidate/social-auth", views.social_auth)
]