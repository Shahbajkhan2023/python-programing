from typing import Any
from django import forms


class FeedBackForm(forms.Form):
    name = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)
    rpassword = forms.CharField(label='Re Enter Password', widget=forms.PasswordInput)
    rollno = forms.IntegerField()
    email = forms.EmailField()
    feedback = forms.CharField(widget=forms.Textarea)
    bot_handler = forms.CharField(required=False, widget=forms.HiddenInput)


    def clean(self):
        total_cleaned_data = super.clean()
        fpwd = total_cleaned_data['password']
        rpwd = total_cleaned_data['rpassword']

        if fpwd != rpwd:
            raise forms.ValidationError('Both password must be matched')
        
        bot_handler_value = total_cleaned_data['bot_handler']
        if len(bot_handler_value) > 0:
            raise forms.ValidationError('request from bot.. cannot be submitted')

