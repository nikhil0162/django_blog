from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse
from .choices import send_choices


class Post(models.Model):
	title = models.CharField(max_length=100)
	content = models.TextField()
	date_posted = models.DateTimeField(default=timezone.now)
	send_via = models.IntegerField(choices=send_choices, default=1) 
	author = models.ForeignKey(User, on_delete=models.CASCADE)

	def __str__(self):
		return self.title

	def get_absolute_url(self):
		return reverse('post-detail', kwargs={'pk': self.pk})
		# return reverse('blog-home')  # if you want to redirect it to home page 

	def save(self, *args, **kwargs):
		super().save()
		self.check_this()

	def check_this(self):
		if self.send_via == 1:
			print('sms')
		elif self.send_via == 2:
			print('email')
		else:
			print('whatsapp')