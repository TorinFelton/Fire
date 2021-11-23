from django import forms
from . import models

class CreateFlame(forms.ModelForm):
	class Meta:
		model = models.Post
		fields = ['title', 'body', 'slug']