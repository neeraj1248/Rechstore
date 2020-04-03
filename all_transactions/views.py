from django.shortcuts import render
from new_entry.models import Entery
from django.db.models import Sum, Min, Max, Avg, Count

# Create your views here.
def all_txn(request):
    rech = Entery.objects.filter(user_name=request.user.username).order_by("-date")

    #To count the total Recharge Amount.
    total_rech_amount = Entery.objects.filter(user_name=request.user.username).aggregate(Sum('rs'))
    for i in total_rech_amount.values():
        r2 = i
    if r2 == None:
        r = 0
    else:
        r = r2

        #To total status amount.
    total_status_amount = Entery.objects.filter(user_name = request.user.username).aggregate(Sum('status'))
    for j in total_status_amount.values():
        s2 = j
    if s2 == None:
        s = 0
    else:
        s = s2


        #taking the balance amount.
    p = r-s
    #to count the total txn amount.
    total_txn = Entery.objects.filter(user_name = request.user.username).aggregate(Count('date'))
    for k in total_txn.values():
        c = k
        #to count the total unpaid txn.
    total_txn_pending = Entery.objects.filter(user_name = request.user.username, p_np = "Not Paid").aggregate(Count('p_np'))
    for l in total_txn_pending.values():
        lp = l
    print("Total Amount : ", r)
    print("Total Status : " ,s)
    print("Balance : " ,p)
    print("total_txn : ", c)
    print("unpaid total : ", lp)

    print(request.user.username)

    #To total Cashback amount.
    total_cb_amount = Entery.objects.filter(user_name = request.user.username).aggregate(Sum('cb'))
    for l in total_cb_amount.values():
        cb1 = l
    if cb1 == None:
        cb1 = 0

    return render(request,'all txn/all_txn.html',{'key1':rech,'total_amount':r, 'total_status':s, 'total_pending': p, 'total_count':c, 'total_unpaid_count':lp,'cb':cb1})

def monthly_statement(request):
    return render(request,'monthly statement/monthly_statement.html')

def extra_pending(request):
    return render (request,'extra pending/extra_pending.html')
