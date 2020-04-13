from django.shortcuts import render,redirect
from manage_ac.models import Customer
from unique_numbers_id.models import Numbers

# Create your views here.
def new_entry_txn(request):
    number = request.POST['number']
    print(number)
    if Numbers.objects.filter(username  = request.user, number = number).exists():
        a = Numbers.objects.get(username  = request.user, number = number)
        a_num = a.number
        a_id = a.ac_id
        a_nam =  a.name
        print(a_num)
        print(a_id)
        print(a_nam)
        return render(request,'new entry/new_entry_txn.html',{'key_num': a_num,'key_nam': a_nam,'key_id': a_id})
    else:
        return render(request,'new entry/new_entry_txn.html',{'key_num': number, 'key1_error_ac_id': 'Number is not registered, Please registered ', 'key_link':'/unique_numbers_id/unique_numbers_id', 'key_text': 'Click here'})

def new_entry(request):
    if request.method =="POST":
        date = request.POST['date']
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
        try:
            pic = request.FILES['pic']
        except KeyError:
            pic = "/No image available.jpg"

        print("User Name : " ,request.user)
        print("Date : " ,date)
        print("Number : ", number)
        print("Name : ", name)
        print("Rs : ", rs)
        print("Status : ", status)
        print("Through : ",through)
        print("Payment : ",payment)
        print("CB :", cb)
        print("APC : ", apc)
        print("Remark : ",remark)
        print("PNP : ",pnp)
        print("AC ID : ", ac_id)
        print("image : ", pic)

        if Customer.objects.filter(ac_id = ac_id).exists():
            from .models import Entery
            ent = Entery(user_name = request.user, date = date, number = number, name = name, rs=rs, status= status, through= through, payment= payment, cb = cb, apc= apc,remark= remark,p_np = pnp, ac_id = ac_id, screenshot = pic)
            ent.save()

            a = Customer.objects.get(user_name = request.user, ac_id = ac_id)
            # for i in a.values():
            ac_bal2 = a.balance
            ac_bal = int(ac_bal2)
            print('Balance : ',ac_bal)
            ac_bal = ((ac_bal+int(rs))-int(status))
            print('Balance After Update : ',ac_bal)
            Customer.objects.filter(user_name = request.user, ac_id = ac_id).update(balance = ac_bal)
            return redirect('entery_saved_succefull')
        else:
            return render(request,'new entry/new_entry.html',{'key1_error_ac_id':'Id is not registered,Please create this is in Customer A/C Section in Setting. or', 'key_link': '/manage_ac/customer_ac_add_del_manage', 'key_text':'Click here'})
    else:
        return render(request,'new entry/new_entry.html')

def saved(request):
    return render(request,'new entry/entery_saved_succefull.html')

def update(request):
    return render(request,'new entry/entery_update_succefull.html')
