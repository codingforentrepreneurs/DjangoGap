from django.contrib import admin

# Register your models here.

from .models import Posting


admin.site.register(Posting)