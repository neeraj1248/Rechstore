from django.urls import path
from . import views

urlpatterns = [
    path('error_404', views.error404, name="error_404")
    # path('login',views.login, name="login"),
]
