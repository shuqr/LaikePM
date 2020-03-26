from django.contrib import admin
from TestModel.models import Test
from TestModel.models import Contact
from TestModel.models import Tag

# Register your models here.
admin.site.register([Test, Contact, Tag])
