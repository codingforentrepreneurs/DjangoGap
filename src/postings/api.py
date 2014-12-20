

from django.contrib.auth import get_user_model


from tastypie.authorization import DjangoAuthorization
from tastypie.authentication import ApiKeyAuthentication, BasicAuthentication, MultiAuthentication
from tastypie.exceptions import BadRequest
from tastypie.models import ApiKey
from tastypie.resources import ModelResource
from tastypie.validation import FormValidation, Validation

from djgap.corsresource import CorsResourceBase


User = get_user_model()


from .forms import PostingForm
from .models import Posting


class PostingValidation(Validation):
    def is_valid(self, bundle, request=None):
        if not bundle.data:
            return {'__all__': 'Not quite what I had in mind.'}

        errors = {}

        for key, value in bundle.data.items():
            if not isinstance(value, basestring):
                continue

            if key == "url":
            	if not 'youtube.com' in value: #or "vimeo.com" in value:
            		print "bad request"
                	errors[key] = ['Submitted URL must be a YouTube URL.']

        return errors



#am1pdGNoZWwzOjEyMw==
class PostingResource(CorsResourceBase, ModelResource):
	class Meta:
		queryset = Posting.objects.all()
		fields = ["user", "title", "url", "id"]
		allowed_method = ['get', 'post']
		resource_name = 'posting'
		authorization = DjangoAuthorization()
		authentication = ApiKeyAuthentication()
		validation = PostingValidation()

	def get_object_list(self, request):
		return super(PostingResource, self).get_object_list(request).\
					filter(user=request.user)

	#curl -v -X POST -d '{"title": "hello there", "url": "http://google.com/"}' -H "Authorization: ApiKey jmitchel3:82de9803f43fcc875e43ebd10d075ad905fa8c26" -H "Content-Type: application/json" http://127.0.0.1:8000/api/v1/posting/
	#curl -v -X POST -d '{"post": "hello there"}' -H "Authorization: ApiKey jmitchel3:82de9803f43fcc875e43ebd10d075ad905fa8c26" -H "Content-Type: application/json" http://127.0.0.1:8000/api/v1/posting/ 
	#curl -v -X POST -d '{"post": "hello there"}' -H "Authorization: ApiKey abc:e3ce77676946d53c6d7b767d1c061426a98f8a2d" -H "Content-Type: application/json" http://127.0.0.1:8000/api/v1/posting/ 
	def hydrate(self, bundle):
		bundle.obj.user = bundle.request.user
		return bundle
	
	# def obj_create(self, bundle, request=None, **kwargs):
	# 	bundle = super(PostingResource, self).obj_create(bundle, kwargs)
	# 	try:
			
	# 		bundle.obj.title = bundle.data.get('title')
	# 		bundle.obj.url = bundle.data.get('url')
	# 		bundle.obj.save()
	# 	except:
	# 		raise BadRequest("Some error with your data.")
	# 	return bundle


	# def dehydrate(self, bundle):
	# 	username = bundle.data.get('username')
	# 	user = User.objects.get(username=username)
	# 	#instance, created = ApiKey.objects.get_or_create(user=user)
	# 	bundle.data['api_key'] = ApiKey.objects.get_or_create(user=user)[0].key
	# 	return bundle