# app/inventory/models.py

# Import from django/third parties modules
from django.db import models

# Import from locals
from app.base.models import AbstractModel

# Create your models here.

# MODEL:Category 
class Category(AbstractModel):

	description = models.CharField(
		max_length=100,
		help_text='Description of the Category',
		unique=True
	)

	def __str__(self):
		return '{}'.format(self.description)

	def save(self):
		self.description = self.description.upper()
		super(Category, self).save()

	class Meta:
		verbose_name_plural = 'Categories'


# MODEL:SubCategory 
class SubCategory(AbstractModel):

	category = models.ForeignKey(Category, on_delete=models.CASCADE)
	description = models.CharField(
		max_length=100,
		help_text='Description of the Sub Category',
	)

	def __str__(self):
		return '{}:{}'.format(self.category.description,self.description)

	def save(self):
		self.description = self.description.upper()
		super(SubCategory, self).save()

	class Meta:
		verbose_name_plural = 'Sub Categories'
		unique_together = ('category','description')