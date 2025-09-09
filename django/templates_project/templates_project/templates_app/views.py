from django.shortcuts import render

# Create your views here.


def index(request):
    return render(request, 'templates_app/index.html')


def other(request):
    return render(request, 'templates_app/other.html')


def base(request):
    return render(request, 'templates_app/base.html')


def relative(request):
    return render(request, 'templates_app/relative.html')

