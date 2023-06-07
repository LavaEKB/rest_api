from django.contrib import admin
from .models import *

class CredcardAdmin(admin.ModelAdmin):
    pass

admin.site.register(Credcard, CredcardAdmin)

