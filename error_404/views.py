from django.shortcuts import render

# Create your views here.
def error404 (request):
    return render(request,'error 404/error 404.html')
