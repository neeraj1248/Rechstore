from django.urls import path
from . import views

urlpatterns = [
    path('txn_update/<int:id>',views.edit, name="txn_update"),
    path('update_record_data/<int:id>',views.update, name="update_record_data")
]
