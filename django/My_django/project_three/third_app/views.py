from django.shortcuts import render
from third_app.models import User

# Create your views here.

def index(request):
    userlist = User.objects.order_by('lastname')
    my_dict = {'users': userlist}
    return render(request, 'third_app/index.html', context=my_dict)