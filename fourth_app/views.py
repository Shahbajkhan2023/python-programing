from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import ContactForm


def contact_view(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            message = form.cleaned_data['message']

            return HttpResponse(f'Thank you {name}, your message has been sent!')
        
    else:
        form = ContactForm()
    
    return render(request, 'forms/contact_page.html', {'form': form})

