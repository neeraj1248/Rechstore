from django.shortcuts import render
from django.db.models import Sum, Min, Max, Avg, Count

# Create your views here.
def balance_record(request):
    from manage_ac.models import Customer
    su = Customer.objects.filter(user_name = request.user.username).aggregate(Sum('balance'))
    for i in su.values():
        su = i
    cust = Customer.objects.filter(user_name = request.user.username)
    print(su)
    return render(request,'bal record/balance_record.html', {'key1_user': cust, 'key_sum': su})
