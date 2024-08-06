from django.shortcuts import render
from django.http import HttpResponse

def form_view(request):
    if request.method == 'POST':
        # Process the form data
        name = request.POST.get('your_name')
        # Do something with the name, like saving it to the database or passing it to the context
        return HttpResponse(f"Hello, {name}!")
    else:
        # Render the form with a default value
        return render(request, 'form.html', {'current_name': 'John Doe'})
