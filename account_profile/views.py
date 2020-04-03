from django.shortcuts import render,redirect
from django.db.models import Sum, Min, Max, Avg, Count
from new_entry.models import Entery

# Create your views here.
def account_pro(request, ac_id):
    global abc_ac_id
    abc_ac_id = ac_id
    from manage_ac.models import Customer
    cust2 = Customer.objects.filter(user_name = request.user.username, ac_id = ac_id)

    from new_entry.models import Entery
    rech_data = Entery.objects.filter(user_name = request.user.username, ac_id = ac_id)
    print(rech_data)

    #sum of total Recharge on this account.
    rech_sum = Entery.objects.filter(user_name = request.user.username, ac_id = ac_id).aggregate(Sum('rs'))
    for rech_sum2 in rech_sum.values():
        rech_sum = rech_sum2
    if rech_sum == None:
        rech_sum = 0

    #sum of the total paid amount in this account.
    rech_status = Entery.objects.filter(user_name = request.user.username, ac_id = ac_id).aggregate(Sum('status'))
    for rech_status2 in rech_status.values():
        rech_status = rech_status2
    if rech_status == None:
        rech_status = 0
        print("Status : ", rech_status)

    #finding the Balance Amount. sum-Status
    rech_bal = rech_sum - rech_status

    #finding the total count of Recharge.
    rech_total_count = Entery.objects.filter(user_name = request.user.username, ac_id = ac_id).aggregate(Count('date'))
    for rech_total_count2 in rech_total_count.values():
        rech_total_count = rech_total_count2
    print(rech_total_count)

    #finding the total count of Unpaid Recharge.
    rech_total_unpaid_count = Entery.objects.filter(user_name = request.user.username, ac_id = ac_id, p_np = "Not Paid").aggregate(Count('p_np'))
    for rech_total_unpaid_count2 in rech_total_unpaid_count.values():
        rech_total_unpaid_count = rech_total_unpaid_count2
    print(rech_total_unpaid_count)

    rech_cb = Entery.objects.filter(user_name = request.user.username, ac_id = ac_id).aggregate(Sum('cb'))
    for rech_cb2 in rech_cb.values():
        rech_cb = rech_cb2
    if rech_cb == None:
        rech_cb = 0
    print("CashBack : ", rech_cb)

    return render(request,'customer ac/ac_preview.html', {'key1_account':cust2, 'key2_rech': rech_data,'key3_sum':rech_sum,'key4_status':rech_status, 'key5_bal': rech_bal,'key6_count':rech_total_count, 'key7_up_count': rech_total_unpaid_count,'key8_cb': rech_cb})


def txn_update(request, id):
    from new_entry.models import Entery
    rech_update = Entery.objects.filter(user_name = request.user.username, id = id)
    print(rech_update)
    return render(request,'customer ac/ac_preview_update.html',{'key1':rech_update})

def update_done(request, id):
    from new_entry.models import Entery
    rech_update = Entery.objects.filter(user_name = request.user.username, id = id)

    if request.method == "POST":
        number = request.POST['number']
        name = request.POST['name']
        rs = request.POST['rs']
        status = request.POST['status']
        through = request.POST['through']
        payment = request.POST['payment']
        cb = request.POST['cb']
        apc = request.POST['apc']
        remark = request.POST['remark']
        pnp = request.POST['pnp']
        ac_id = request.POST['ac_id']
        check = request.POST.getlist('check[]')
        print('Check value',check)

        a = Entery.objects.get(user_name = request.user, id = id)
        a_status = a.status
        print('Status : ', a_status)
        
        from manage_ac.models import Customer

        a_bal = Customer.objects.get(user_name = request.user, ac_id = ac_id)
        ac_bal2 = a_bal.balance
        ac_bal = int(ac_bal2)
        print('Balance : ',ac_bal)
        ac_bal = ((ac_bal+int(a_status))-int(status))
        print('Balance After Update : ',ac_bal)
        Customer.objects.filter(user_name = request.user, ac_id = ac_id).update(balance = ac_bal)

        Entery.objects.filter(user_name = request.user.username, id=id).update(number = number, name= name, rs=rs, status=status, through= through, payment= payment, cb=cb, apc=apc, remark=remark,p_np=pnp, ac_id= ac_id)



        from manage_ac.models import Customer
        cust2 = Customer.objects.filter(user_name = request.user.username, ac_id = abc_ac_id)

        from new_entry.models import Entery
        rech_data = Entery.objects.filter(user_name = request.user.username, ac_id = abc_ac_id)
        print(rech_data)

        #sum of total Recharge on this account.
        rech_sum = Entery.objects.filter(user_name = request.user.username, ac_id = abc_ac_id).aggregate(Sum('rs'))
        for rech_sum2 in rech_sum.values():
            rech_sum = rech_sum2
        if rech_sum == None:
            rech_sum = 0

        #sum of the total paid amount in this account.
        rech_status = Entery.objects.filter(user_name = request.user.username, ac_id = abc_ac_id).aggregate(Sum('status'))
        for rech_status2 in rech_status.values():
            rech_status = rech_status2
        if rech_status == None:
            rech_status = 0
            print("Status : ", rech_status)

        #finding the Balance Amount. sum-Status
        rech_bal = rech_sum - rech_status

        #finding the total count of Recharge.
        rech_total_count = Entery.objects.filter(user_name = request.user.username, ac_id = abc_ac_id).aggregate(Count('date'))
        for rech_total_count2 in rech_total_count.values():
            rech_total_count = rech_total_count2
        print(rech_total_count)

        #finding the total count of Unpaid Recharge.
        rech_total_unpaid_count = Entery.objects.filter(user_name = request.user.username, ac_id = abc_ac_id, p_np = "Not Paid").aggregate(Count('p_np'))
        for rech_total_unpaid_count2 in rech_total_unpaid_count.values():
            rech_total_unpaid_count = rech_total_unpaid_count2
        print(rech_total_unpaid_count)

    return render(request,'customer ac/ac_preview.html', {'key1_account':cust2, 'key2_rech': rech_data,'key3_sum':rech_sum,'key4_status':rech_status, 'key5_bal': rech_bal,'key6_count':rech_total_count, 'key7_up_count': rech_total_unpaid_count})
