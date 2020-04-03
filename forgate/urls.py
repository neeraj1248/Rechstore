from django.urls import path
from . import views

urlpatterns = [
    path('resataccountpassword',views.forgatepage, name="resataccountpassword"),
    path('forgateotppage', views.forgateotppage, name="forgateotppage"),
    path('newpassword', views.newpassword, name="newpassword"),
    # path('login',views.login, name="login"),
]
