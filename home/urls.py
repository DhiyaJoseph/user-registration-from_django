from .import views
from django.urls import path,include

urlpatterns = [
    path('',views.index,name="index"),
    path('signup',views.signup,name="signup"),
    path('login',views.loginn,name="login"),
]