from django.shortcuts import render, redirect
from django.contrib import messages
from . import forms  # Adjust import according to your project structure


def student_view(request):
    if request.method == 'POST':
        form = forms.StudentForm(request.POST)
        if form.is_valid():
            form.save(commit=True)
            # Add a success message
            messages.success(request, 'Student information has been successfully saved!')
            # Redirect to the thank you page
            return redirect('thank_you')  # Redirect to the 'thank_you' URL pattern name
    else:
        form = forms.StudentForm()

    return render(request, 'seventhapp/student_form.html', {'form': form})


def thank_you_view(request):
    return render(request, 'seventhapp/thank_you.html')