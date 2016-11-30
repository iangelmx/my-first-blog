from django.db import models
from django.utils import timezone
from django.contrib.auth.models import AbstractUser

class Post(models.Model):
	author = models.ForeignKey('auth.User')
	title = models.CharField(max_length = 200)
	text = models.TextField()
	created_date = models.DateTimeField(
		default=timezone.now)
	published_date = models.DateTimeField(
		blank=True, null=True)

	def publish(self):
		self.published_date=timezone.now()
		self.save()

	def __str__(self):
		return self.title


"""
 class CustomUsers(AbstractUser):
	type_choices = (
	('SU', 'Super User'),
	('A', 'User Type A'),
	('B', 'User Type B'),
	('C', 'User Type C'),
	)
	user_type = models.CharField(max_length=2, choices = type_choices, default='C')

class UserDetails (models.Model):
	type=models.OneToOneField('CustoUser')
	extra_info = models.CharField(max_length = 2)"""

# Create your models here.
