from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login as auth_login
from GoldPricePrediction.views import  *

def login(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, request.POST)
        if form.is_valid():
            user = form.get_user()
            auth_login(request, user)
            return redirect('home')  # Redirect to home page after successful login
    else:
        form = AuthenticationForm()
    return render(request, 'GoldPricePrediction/login.html', {'form': form})




# login/views.py

# from django.shortcuts import render
# from django.contrib.auth.decorators import login_required

# @login_required
# def home(request):
#     # Your logic to render the home page
#     return render(request, 'GoldPricePrediction/home.html')  # Adjust as needed
