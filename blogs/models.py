from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class BlogPost(models.Model):
	""" A blog the user has posted. """

	title = models.CharField(max_length=100)
	text = models.TextField(max_length=1000)
	date_added = models.DateTimeField(auto_now_add=True)
	owner = models.ForeignKey(User, on_delete=models.CASCADE)


	def __str__(self):
		"""Return a string representation of the model."""
		
		if len(self.text) >= 50:
			return f'{self.title} {self.text[:50]}...'

		else:
			return f'{self.title} {self.text}'