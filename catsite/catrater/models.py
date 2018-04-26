from django.db import models
from django.utils import timezone

# Create your models here.

class Cat(models.Model):
	owner = models.ForeignKey('auth.User', on_delete=models.CASCADE)
	name = models.CharField(max_length=200)
	description = models.CharField(max_length=500)
	photo = models.ImageField(max_length=150)
	upload_date = models.DateTimeField(blank=True, null=True)
	hearts = models.IntegerField()

	def upload(self):
		self.upload_date = timezone.now()
		self.save()

	def __str__(self):
		return self.name


