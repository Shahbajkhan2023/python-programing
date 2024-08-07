from django.shortcuts import render
from .forms import AddressForm


def address_view(request):
    if request.method == 'POST':
        form = AddressForm(request.POST)
        if form.is_valid():
            # Process the form data here
            return render(request, 'fifth_app/thank_you.html')
    else:
        form = AddressForm()

    return render(request, 'fifth_app/address_form.html', {'form': form})

