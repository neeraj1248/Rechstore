from django.urls import path
from . import views

urlpatterns = [
    path('login', views.login, name="login"),
    path('register', views.register, name="register"),
    path('registration_validation', views.validation, name="registration_validation"),
    path('activating_user', views.activating_user, name="activating_user"),
    path('validate_token', views.validate_token, name='validate_token'),

]
