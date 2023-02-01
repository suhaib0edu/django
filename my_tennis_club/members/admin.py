from django.contrib import admin
from .models import *

# Register your models here.
class MemberAdmin(admin.ModelAdmin):
    list_display = ['id','firstname','lastname','joined_date']
    list_display_links = ['id']
admin.site.register(Member,MemberAdmin)