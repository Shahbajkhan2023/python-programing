from typing import Any
from django import forms


# class FeedBackForm(forms.Form):
#     name = forms.CharField()
#     rollno = forms.IntegerField()
#     email = forms.EmailField()
#     feedback = forms.CharField(widget=forms.Textarea)

#     def clean_name(self):
#         input_name = self.cleaned_data['name']
#         if len(input_name) < 4:
#             raise forms.ValidationError('The Minimum no of characters in the name fied shourd be 4')
#         return input_name
    
#     def clean_rollno(self):
#         input_rollno = self.cleaned_data['rollno']
#         print('validating rollno field')
#         return input_rollno
    
#     def clean_email(self):
#         input_email = self.cleaned_data['email']
#         print('validating email field')
#         return input_email
    
#     def clean_feedback(self):
#         input_feedback = self.cleaned_data['feedback']
#         print('validating the feedback.')
#         return input_feedback

from django.core import validators


# class FeedBackForm(forms.Form):
#     name = forms.CharField()
#     rollno = forms.IntegerField()
#     email = forms.EmailField()
#     feed_bak = forms.CharField(widget=forms.Textarea, validators=[validators.MaxLengthValidator(40)])




# def start_with_d(value):
#     if value[0].lower() != 'd':
#         raise forms.ValidationError('name should be start with d | D')


# class FeedBackForm(forms.Form):
#     name = forms.CharField(validators=[start_with_d])
#     rollno = forms.IntegerField()
#     email = forms.EmailField()
#     feed_back = forms.CharField(widget=forms.Textarea)




# class FeedBackForm(forms.Form):
#     name = forms.CharField()
#     rollno = forms.IntegerField()
#     email = forms.EmailField()
#     feed_back = forms.CharField(widget=forms.Textarea)

#     def clean(self):
#         print('Total form validation')
#         total_cleaned_data = super.clean()
#         inputname = total_cleaned_data['name']
#         if inputname[0].lower() != 'd':
#             raise forms.ValidationError('name parameter should start with d')
#         inputrollno = total_cleaned_data['rollno']
#         if inputrollno <= 0:
#             raise forms.ValidationError('Rollno should be > 0')
        

class FeedBackForm(forms.Form):
    name = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)
    rpassword = forms.CharField(label='Re Enter Password', widget=forms.PasswordInput)
    rollno = forms.IntegerField()
    email = forms.EmailField()
    feedback = forms.CharField(widget=forms.Textarea)

    def clean(self):
        print('validating password match...')
        total_cleaned_data = super().clean()
        fpwd = total_cleaned_data['password']
        spwd = total_cleaned_data['rpassword']
        if fpwd != spwd:
            raise forms.ValidationError('Both password must be match')
        
        