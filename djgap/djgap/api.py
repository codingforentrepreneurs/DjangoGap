

from tastypie.models import ApiKey
from tastypie.authorization import DjangoAuthorization
from tastypie.authentication import ApiKeyAuthentication, BasicAuthentication, MultiAuthentication
from tastypie.resources import ModelResource

from django.contrib.auth import get_user_model
from .corsresource import CorsResourceBase

User = get_user_model()

#am1pdGNoZWwzOjEyMw==
class LoginResource(CorsResourceBase, ModelResource):
	class Meta:
		queryset = User.objects.all()
		fields = ["first_name", "last_name", "username"]
		allowed_method = ['get']
		resource_name = 'login'
		authorization = DjangoAuthorization()
		authentication = BasicAuthentication()

	def dehydrate(self, bundle):
		username = bundle.data.get('username')
		user = User.objects.get(username=username)
		#instance, created = ApiKey.objects.get_or_create(user=user)
		bundle.data['api_key'] = ApiKey.objects.get_or_create(user=user)[0].key
		return bundle