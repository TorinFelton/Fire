from django.shortcuts import render, redirect
from .models import Flame
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from . import forms

# Create your views here.

def home(request):
	flames = Flame.objects.all().order_by('date')

	return render(request, 'firehome/home.html', {'flames': flames})

def flame_detail(request, post):
	# return HttpResponse(post)
	flame = Flame.objects.get(slug=post)
	return render(request, 'firehome/fire_post.html', {'post': flame})

@login_required(login_url="/accounts/login")
def flame_create(request):
	if request.method == 'POST':
		form = forms.CreateFlame(request.POST)
		if form.is_valid():
			return redirect('/firehome/')
	else:
		form = forms.CreateFlame()
	return render(request, 'firehome/flame_create.html', {'form': form})