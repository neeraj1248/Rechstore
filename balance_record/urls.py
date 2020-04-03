from django.urls import path
from . import views

urlpatterns = [
    path('balance_record',views.balance_record, name="balance_record"),
]
