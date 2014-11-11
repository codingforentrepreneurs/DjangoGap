from django.conf import settings
from django.db import models
from django.utils import timezone
# Create your models here.
class Posting(models.Model):
	user = models.ForeignKey(settings.AUTH_USER_MODEL)
	post = models.CharField(max_length=500)
	timestamp = models.DateTimeField(auto_now_add=True, auto_now=False, default=timezone.now())
	updated = models.DateTimeField(auto_now_add=False, auto_now=True, default=timezone.now())

	def __unicode__(self):
		return self.post[:10]
	
	class Meta:
		ordering = ['-updated', '-timestamp']
