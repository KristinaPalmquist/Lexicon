from django.contrib import admin
from AppTwo.models import AccessRecord, Topic, WebPage, UserProfile
# Register your models here.


admin.site.register(AccessRecord)
admin.site.register(Topic)
admin.site.register(WebPage)
admin.site.register(UserProfile)
