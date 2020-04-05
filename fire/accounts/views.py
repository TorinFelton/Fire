from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, logout

def signup_view(request):
	if request.method == 'POST':
		form = UserCreationForm(request.POST)
		if form.is_valid():
			user = form.save() # Create account
			login(request, user)
			return redirect('/firehome/')
	else:
		form = UserCreationForm()
	return render(request, 'accounts/signup.html', {'form': form})


def login_view(request):
	if request.method == 'POST':
		form = AuthenticationForm(data=request.POST)
		if form.is_valid():
			# login
			user = form.get_user()
			login(request, user)
			toRedirect = '/firehome/'
			if 'next' in request.POST:
				toRedirect = request.POST.get('next')
			return redirect(toRedirect)
	else:
		form = AuthenticationForm()
	return render(request, "accounts/login.html", {'form': form})

def logout_view(request):
	if request.method == 'POST':
		logout(request)
		return redirect('/firehome/')