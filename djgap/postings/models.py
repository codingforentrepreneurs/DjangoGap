from django.conf import settings
from django.db import models

# Create your models here.
class Posting(models.Model):
	user = models.ForeignKey(settings.AUTH_USER_MODEL)
	post = models.CharField(max_length=500)

	def __unicode__(self):
		return self.post[:10]