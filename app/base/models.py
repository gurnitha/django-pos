# app/base/models.py

# Import from django/third parties modules
from django.db import models
from django.contrib.auth.models import User 

# Import from locals

# Create your models here.


class AbstractModel(models.Model):

	"""
	AbstractModel.
	Model ini tidak akan nampak, karena kelas ini 
	tidak bisa dijalankan dengan perintah makemigrations
	dan migrate.

	Model ini adalah sebuah Model layaknya sebuah 'pola'
	yang bisa digunakan oleh Model-model lainnya di dalam
	aplikasi ini.

	Intinya, field yang ada dalam AbstractModel ini,
	akan tersedia secara otomatis (DRF) bila
	AbstractModel ini digunakan oleh Model lain
	yang akan dibuat.
	"""

	state = models.BooleanField(default=True)
	date_created = models.DateTimeField(auto_now_add=True)
	date_modified = models.DateTimeField(auto_now=True)
	user_creation = models.ForeignKey(User,on_delete=models.CASCADE)
	user_modification = models.IntegerField(blank=True,null=True)

	class Meta:
		abstract = True