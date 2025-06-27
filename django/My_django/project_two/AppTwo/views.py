from django.shortcuts import render
# from django.http import HttpResponse
from AppTwo.models import AccessRecord

# Create your views here.


def index(request):
    webpage_list = AccessRecord.objects.order_by('date')
    date_dict = {'access_records': webpage_list}
    return render(request, 'AppTwo/index.html', context=date_dict)


def help(request):
    return render(request, 'AppTwo/help.html')
