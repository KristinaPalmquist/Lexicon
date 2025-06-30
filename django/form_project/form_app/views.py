from django.shortcuts import render
from form_app.models import Message
from form_app.forms import ContactForm

def index(request):
    return render(request, 'form_app/index.html')

def contact(request):
    form = ContactForm()
    
    if request.method == 'POST':
        form = ContactForm(request.POST)
        
        if form.is_valid():
            print('Name: ' + form.cleaned_data['name'])
            print('Email: ' + form.cleaned_data['email'])
            print('Message: ' + form.cleaned_data['message'])
            
            form.save(commit=True)
            return submissions(request)
        else:
            print('Invalid form. ERROR!')
    return render(request, 'form_app/contact.html', {'form': form})

def submissions(request):
    messageList = Message.objects.order_by('name')
    message_dict = {'messages': messageList}
    return render(request, 'form_app/submissions.html', context=message_dict)

