from django.contrib import admin
from .models import *
# Register your models here.
admin.site.register(News)
admin.site.register(SportNews)
admin.site.register(BreakingNews)
admin.site.register(NewsDate)
admin.site.register(RegistrationData)

