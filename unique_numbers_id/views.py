from django.shortcuts import render,redirect
from django.db.models import Sum, Min, Max, Avg, Count

# Create your views here.
def number(request):
    if request.method=='POST':
        number = request.POST['number']
        name = request.POST['name']
        ac_id = request.POST['ac_id']

        from .models import Numbers
        x = Numbers(number = number, name = name, ac_id = ac_id, username = request.user)
        x.save()
        return redirect('saved')
    else:
        from .models import Numbers
        rech = Numbers.objects.filter(username = request.user)
        number_count = Numbers.objects.filter(username = request.user).aggregate(Count('id'))
        for i in number_count.values():
            n_c = i
        return render(request,'number record/numbers.html',{'key1': rech, 'key2': n_c})

def number_saved(request):
    from .models import Numbers
    rech = Numbers.objects.filter(username = request.user)
    return render(request,'number record/numbers.html',{'key1': rech})
