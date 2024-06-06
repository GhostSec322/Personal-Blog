from django.shortcuts import render,redirect
def BASE(request):
    return render(request,'Main/main.html')

def INDEX(request):
    return render(request,'Main/index.html')