from django.shortcuts import render


def index(request):
    my_dict = {
        'insert_me': (
            'Hello from views.py. This text is sent in with the html-template '
            'when the view is created.'
        )
    }
    return render(request, 'app_1/index.html', context=my_dict)
