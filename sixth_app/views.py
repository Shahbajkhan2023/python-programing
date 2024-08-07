from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import FeedBackForm


def feedback_view(request):
    if request.method == 'POST':
        form = FeedBackForm(request.POST)
        if form.is_valid():
            # Handle successful form submission (e.g., save data, send email)
            messages.success(request, 'Thank you for your feedback! Your form was submitted successfully.')
            return redirect('feedback')  # Redirect to avoid form resubmission on refresh
        else:
            # If form is invalid, show error message
            messages.error(request, 'Passwords do not match. Please try again.')
            return redirect('feedback')
    else:
        form = FeedBackForm()

    return render(request, 'feedback/feedback_form.html', {'form': form})
