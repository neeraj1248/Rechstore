from django.urls import path
from . import views

urlpatterns = [
    path('all_txn',views.all_txn, name="all_txn"),
    path('monthly_statement',views.monthly_statement, name="monthly_statement"),
    path('extra_pending',views.extra_pending, name="extra_pending"),
]
