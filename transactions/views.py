from django.shortcuts import render,redirect
from new_entry.models import Entery
from manage_ac.models import Customer
# Create your views here.
def edit(request, id):

    # print(username1)
    # print(username2)
    # print(username1 is username2)
    #
    # a = Entery.objects.filter(user_name = request.user).values('id')
    # print(len(a))
    # d = len(a)
    # print(id)
    if Entery.objects.filter(id = id).exists():
        y = Entery.objects.get(id= id)
        username1 = str(y.user_name)
        username2 = str(request.user)
        if username1 == username2:
            edit_data = Entery.objects.get(id = id)
            return render(request,'new entry/edit_entry.html',{'key_edit':edit_data})
        else:
            return redirect('error_404')
    else:
        return redirect('error_404')

def update(request,id):
    if request.method=="POST":
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



        a = Entery.objects.get(user_name = request.user, id = id)
        a_status = a.status
        print('Status : ', a_status)

        a_bal = Customer.objects.get(user_name = request.user, ac_id = ac_id)
        ac_bal2 = a_bal.balance
        ac_bal = int(ac_bal2)
        print('Balance : ',ac_bal)
        ac_bal = ((ac_bal+int(a_status))-int(status))
        print('Balance After Update : ',ac_bal)
        Customer.objects.filter(user_name = request.user, ac_id = ac_id).update(balance = ac_bal)

        Entery.objects.filter(id=id).update(number = number, name= name, rs=rs, status=status, through= through, payment= payment, cb=cb, apc=apc, remark=remark,p_np=pnp, ac_id= ac_id )
        return redirect('entery_update_succefull')
