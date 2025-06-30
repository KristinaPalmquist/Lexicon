from django.shortcuts import render
from app_3.models import User


def users(request):
    userlist = User.objects.order_by('lastname')
    my_dict = {'users': userlist}
    return render(request, 'app_3/users.html', context=my_dict)