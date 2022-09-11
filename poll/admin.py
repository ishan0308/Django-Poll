from django.contrib import admin
import site
from . import models
# Register your models here.

class apollAdmin(admin.ModelAdmin):
    list_display = ('question','timestamp')
admin.site.register(models.apollModel,apollAdmin)

