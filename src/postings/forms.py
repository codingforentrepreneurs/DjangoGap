from django import forms


from .models import Posting

class PostingForm(forms.ModelForm):
	class Meta:
		model = Posting
		fields = ['title', 'url']

	def clean_url(self):
		url = self.cleaned_data.get('url')
		if not "youtube.com" in url:
			print "error"
		return url