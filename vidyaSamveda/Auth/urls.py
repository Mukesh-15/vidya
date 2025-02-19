
from django.urls import path
from .views import *

urlpatterns = [
    path('',login,name="login"),
    path('signup',signup),
    path('forgot_pass',forgot_password),
    path('intern_post',intern_post),
    path('register',signin,name='register'),
    path('recruit_regis',recruit_regis),
    path('internship_view',internship_view)
]
