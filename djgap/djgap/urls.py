from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.views.generic import TemplateView

from tastypie.api import Api

from .api import LoginResource
from postings.api import PostingResource

v1_api = Api(api_name='v1')
v1_api.register(LoginResource())
v1_api.register(PostingResource())

urlpatterns = patterns('',
    # Examples:
    url(r'testing/', TemplateView.as_view(template_name="ajax_testing.html")),
    url(r'^api/', include(v1_api.urls)),
    url(r'^$', 'djgap.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
)
