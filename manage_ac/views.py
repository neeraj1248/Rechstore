from django.shortcuts import render,redirect

# Create your views here.
def ac_add(request):
    from .models import Customer
    if request.method == 'POST':
            number = request.POST['number']
            name = request.POST['name']
            ac = request.POST['acid']

            if Customer.objects.filter(ac_id = ac, user_name = request.user.username).exists():
                return redirect('error_id_having')
                # return render(request,'manage ac/manage_ac.html', {'error_key':'Account Id is already exists, Please choose another id.'})

            else:
                if Customer.objects.filter(number = number, user_name = request.user.username).exists():
                    return redirect('error_id_having_number')
                else:
                    x = Customer(user_name = request.user, number = number, name = name, ac_id = ac)
                    x.save()
                    return redirect('userregisterd')
    else:
        from .models import Customer
        data = Customer.objects.filter(user_name = request.user.username)
        return render(request,'manage ac/manage_ac.html', {'acdata': data})

def error_id(request):
    from .models import Customer
    data = Customer.objects.filter(user_name = request.user.username)
    return render(request,'manage ac/manage_ac.html', {'error_key':'Account Id is already exists, Please choose another id.','acdata': data})

def error_id_number(request):
    from .models import Customer
    data = Customer.objects.filter(user_name = request.user.username)
    return render(request,'manage ac/manage_ac.html', {'error_key':'Number is already registered.','acdata': data})

def user_register(request):
    from .models import Customer
    data = Customer.objects.filter(user_name = request.user.username)
    return render(request,'manage ac/manage_ac.html', {'error_key':'Account Registered Succefully.','acdata': data})
