from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, logout
from . import forms

def signup_view(request):

	if request.method == 'POST':
		form = forms.UserSignupForm(request.POST)
		if len(form.errors) > 0:
			form.formattedErrors = []
			for error_field in form.errors.as_data():
				for error in form.errors.as_data()[error_field]:
					form.formattedErrors.append((str(error)[:len(str(error))-2])[2:])
		if form.is_valid():
			user = form.save() # Create account
			login(request, user)
			return redirect('/firehome/')
	else:
		form = forms.UserSignupForm()
	return render(request, 'accounts/signup.html', {'form': form})


def login_view(request):
	if request.method == 'POST':
		form = forms.UserLoginForm(data=request.POST)
		if form.is_valid():
			# login
			user = form.get_user()
			login(request, user)
			toRedirect = '/firehome/'
			if 'next' in request.POST:
				toRedirect = request.POST.get('next')
			return redirect(toRedirect)
	else:
		form = forms.UserLoginForm()
	return render(request, "accounts/login.html", {'form': form})

def logout_view(request):
	if request.method == 'POST':
		logout(request)
		return redirect('/firehome/')