from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Post(models.Model):
	title = models.CharField(max_length=100)
	body = models.TextField()
	slug = models.SlugField(default='firepost')
	date = models.DateTimeField(auto_now_add=True)
	author = models.ForeignKey(User, default=None, on_delete=models.DO_NOTHING)

	def __str__(self):
		return self.title

	def snippet(self):
		if len(self.body) > 100:
			toReturn = self.body[:100]
		else:
			toReturn = self.body
		return toReturn
	def isLong(self):
		return len(self.body) > 100