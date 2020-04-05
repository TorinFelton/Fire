from django.db import models

# Create your models here.

class Flame(models.Model):
	title = models.CharField(max_length=100)
	body = models.TextField()
	slug = models.SlugField(default='firepost')
	date = models.DateTimeField(auto_now_add=True)
	# todo thumbnail, author

	def __str__(self):
		return self.title

	def snippet(self):
		return self.body[:100]