from django.urls import path
from . import views

urlpatterns = [
    path('account/<int:ac_id>', views.account_pro, name="account"),
    path('txn_update/<int:id>', views.txn_update, name="txn_update"),
    path('txn_update_done/<int:id>',views.update_done, name="txn_update_done"),
]
