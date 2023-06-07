from django.contrib import admin
from .models import Sale

class PostAdmin(admin.ModelAdmin):
    pass

admin.site.register(Sale, PostAdmin)
