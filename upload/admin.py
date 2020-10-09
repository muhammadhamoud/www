from django.contrib import admin

# Register your models here.

from .models import Future, DataReport, ImportFiles

admin.site.register(Future)
admin.site.register(DataReport)
admin.site.register(ImportFiles)