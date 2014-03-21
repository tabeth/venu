from django.db import models
import valentine

# Create your models here.
class Food(models.Model):
	name = models.CharField(max_length=128, unique=True)

	def __unicode__(self):
		return self.name