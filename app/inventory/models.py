# app/inventory/models.py

# Import from django/third parties modules
from django.db import models

# Import from locals
from app.base.models import AbstractModel

# Create your models here.

class Category(AbstractModel):

	description = models.CharField(
		max_length=100,
		help_text='Description of the Category',
		unique=True
	)

	def __str__(self):
		return '{}'.format(self.description)

	def save():
		self.description = self.description.upper()
		super(Category, self).save()

	class Meta:
		verbose_name_plural = 'Categories'