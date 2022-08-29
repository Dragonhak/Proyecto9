from enum 							import unique
from django.db 						import models
from django.contrib.auth.models 	import AbstractUser

class Usuario(AbstractUser):
	
	dni = models.IntegerField(null=True, unique=True)

	class Meta:
		db_table="usuarios"
		ordering = ["first_name", "last_name"] 

	def __str__(self):
		return self.get_full_name()

