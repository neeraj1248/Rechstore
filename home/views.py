from django.shortcuts import render,redirect
from new_entry.models import Entery
from django.db.models import Sum, Min, Max, Avg, Count

# Create your views here.
def home(request):
    rech = Entery.objects.filter(user_name=request.user.username).order_by('-date','-id')[:20]
    rech3 = rech
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

    #to count the total txn amount.
    total_txn = Entery.objects.filter(user_name = request.user.username).aggregate(Count('date'))
    for k in total_txn.values():
        c = k

        #to count the total unpaid txn.
    total_txn_pending = Entery.objects.filter(user_name = request.user.username, p_np = "Not Paid").aggregate(Count('p_np'))
    for l in total_txn_pending.values():
        lp = l

        #to count the total paid txn.
    total_txn_paid = Entery.objects.filter(user_name = request.user.username, p_np = "Paid").aggregate(Count('p_np'))
    for m in total_txn_paid.values():
        pt = m

        #finding the bal.
        p = r-s
        print('Pending the = ',p)

        #counting the persentage in total paid amount.
    if r==0:
        r=1

    per = ((p*100)/r)
    per2 = int(per)
    print(per2)

    #To total Cashback amount.
    total_cb_amount = Entery.objects.filter(user_name = request.user.username).aggregate(Sum('cb'))
    for l in total_cb_amount.values():
        cb1 = l
    if cb1 == None:
        cb1 = 0

    return render(request,'home/home.html', {'key1':rech3,'total_amount':r, 'total_status':s, 'total_pending': p, 'total_count':c, 'total_unpaid_count':lp,'total_paid_count':pt,'persen':per2,'cb':cb1})

def logout(request):
    from django.contrib import auth
    auth.logout(request)
    return redirect('login')

# def login(request):
#     return render(request,'login/login.html')
