from django.shortcuts import render, redirect
from .forms import ContactForm  # Ensure you have the correct path to your form

def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()  # This saves the data to the ContactSubmission model
            return redirect('success')  # Redirects to the 'success' URL name
    else:
        form = ContactForm()
    return render(request, 'GoldPricePrediction/contact.html', {'form': form})


from django.shortcuts import render

def success_view(request):
    return render(request, 'GoldPricePrediction/contact.html')
