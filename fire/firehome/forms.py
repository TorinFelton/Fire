from django import forms
from . import models

class CreateFlame(forms.ModelForm):
	class Meta:
		model = models.Flame
		fields = ['title', 'body', 'slug']