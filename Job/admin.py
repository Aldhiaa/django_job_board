from django.contrib import admin
# Register your models here.
from .models import job,Category,Apply
admin.site.register(job)
admin.site.register(Category)
admin.site.register(Apply)