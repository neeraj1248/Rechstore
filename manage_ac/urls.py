from django.urls import path
from . import views

urlpatterns = [
    path('customer_ac_add_del_manage',views.ac_add, name="customer_ac_add_del_manage"),
    path('error_id_having',views.error_id, name='error_id_having'),
    path('error_id_having_number',views.error_id_number, name='error_id_having_number'),
    path('userregisterd',views.user_register, name="userregisterd"),
]
