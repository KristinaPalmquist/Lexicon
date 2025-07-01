from django.shortcuts import render


def home(request):
    return render(request, 'lab_app/home.html')

def about(request):
    return render(request, 'lab_app/about.html')


