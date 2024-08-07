from django import forms


class AddressForm(forms.Form):
    street = forms.CharField(max_length=100)
    city = forms.CharField(max_length=50)
    state = forms.CharField(max_length=20)
    zip_code = forms.CharField(max_length=10)


    