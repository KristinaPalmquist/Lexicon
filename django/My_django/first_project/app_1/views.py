from django.shortcuts import render



def index(request):
    my_dict = {'insert_me': 'Hello from views.py'}
    return render(request, 'app_1/index.html', context=my_dict)
