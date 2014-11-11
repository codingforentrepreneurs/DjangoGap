

from django.contrib.auth import get_user_model


from tastypie.authorization import DjangoAuthorization
from tastypie.authentication import ApiKeyAuthentication, BasicAuthentication, MultiAuthentication
from tastypie.exceptions import BadRequest
from tastypie.models import ApiKey
from tastypie.resources import ModelResource



User = get_user_model()


from .models import Posting
#am1pdGNoZWwzOjEyMw==
class PostingResource(ModelResource):
	class Meta:
		queryset = Posting.objects.all()
		fields = ["user", "post"]
		allowed_method = ['get', 'post']
		resource_name = 'posting'
		authorization = DjangoAuthorization()
		authentication = ApiKeyAuthentication()

	def get_object_list(self, request):
		return super(PostingResource, self).get_object_list(request).\
					filter(user=request.user)



	#curl -v -X POST -d '{"post": "hello there"}' -H "Authorization: ApiKey jmitchel3:82de9803f43fcc875e43ebd10d075ad905fa8c26" -H "Content-Type: application/json" http://127.0.0.1:8000/api/v1/posting/ 
	#curl -v -X POST -d '{"post": "hello there"}' -H "Authorization: ApiKey abc:e3ce77676946d53c6d7b767d1c061426a98f8a2d" -H "Content-Type: application/json" http://127.0.0.1:8000/api/v1/posting/ 

	def obj_create(self, bundle, request=None, **kwargs):
		try:
			bundle.obj.user = bundle.request.user
			bundle.obj.post = bundle.data.get('post')
			bundle.obj.save()
		except:
			raise BadRequest("Some error with your data.")
		return bundle


	# def dehydrate(self, bundle):
	# 	username = bundle.data.get('username')
	# 	user = User.objects.get(username=username)
	# 	#instance, created = ApiKey.objects.get_or_create(user=user)
	# 	bundle.data['api_key'] = ApiKey.objects.get_or_create(user=user)[0].key
	# 	return bundle