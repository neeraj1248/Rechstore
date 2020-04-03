from django.urls import path
from . import views

urlpatterns = [
    path('unique_numbers_id',views.number,name='unique_numbers_id'),
    path('saved', views.number_saved, name='saved'),
]
