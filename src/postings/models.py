from django.conf import settings
from django.db import models
from django.utils import timezone
# Create your models here.
class Posting(models.Model):
	user = models.ForeignKey(settings.AUTH_USER_MODEL)
	#post = models.CharField(max_length=500)
	title = models.CharField(max_length=200, default='Title')
	url = models.URLField(max_length=400, default='http://youtube.com/')
	timestamp = models.DateTimeField(auto_now_add=True, auto_now=False, default=timezone.now())
	updated = models.DateTimeField(auto_now_add=False, auto_now=True, default=timezone.now())

	def __unicode__(self):
		return self.title[:10]
	
	class Meta:
		ordering = ['-updated', '-timestamp']
