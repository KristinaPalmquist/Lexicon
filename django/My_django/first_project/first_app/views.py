from django.shortcuts import render
# from django.http import HttpResponse
# from django.template import loader


# Create your views here.


def index(request):
    my_dict = {'insert_me': 'Hello from views.py'}
    # template = loader.get_template('index.html')
    # return HttpResponse(template.render())
    return render(request, 'index.html', context=my_dict)
