from django.urls import path
from . import views

urlpatterns = [
    path('new_entry',views.new_entry, name="new_entry"),
    path('new_entry_txn', views.new_entry_txn, name="new_entry_txn"),
    path('entery_saved_succefull',views.saved, name = 'entery_saved_succefull'),
    path('entery_update_succefull',views.update, name="entery_update_succefull"),
]
