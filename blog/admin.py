from django.contrib import admin
from . import models as blogModels
from polls import models as pollModels

# Register your models here.
admin.site.register(blogModels.Topic)
admin.site.register(blogModels.Entry)
admin.site.register(blogModels.Author)
admin.site.register(pollModels.Question)
admin.site.register(pollModels.Choice)