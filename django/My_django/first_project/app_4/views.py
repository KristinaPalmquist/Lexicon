from django.shortcuts import render
from . import forms

def index(request):
    return render(request, 'app_4/index.html')


def form_name_view(request):
    form = forms.FormName()
    if request.method == 'POST':
        form = forms.FormName(request.POST)
        if form.is_valid():
            print('Validation success!!!')
            print('Name: ' + form.cleaned_data['name'])
            print('Email: ' + form.cleaned_data['email'])
            print('Text: ' + form.cleaned_data['text'])
            # form.save(commit=True)
            return index(request)
        else:
            print('error form invalid')
    # return render(request, 'app_4/index.html')
        
    return render(request, 'app_4/form_page.html', {'form': form})
