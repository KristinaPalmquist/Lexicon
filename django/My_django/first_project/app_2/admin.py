from django.contrib import admin
from app_2.models import AccessRecord, Topic, WebPage, UserProfile
# Register your models here.


admin.site.register(AccessRecord)
admin.site.register(Topic)
admin.site.register(WebPage)
admin.site.register(UserProfile)
