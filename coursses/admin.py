from django.contrib import admin
from django_summernote.admin import SummernoteModelAdmin
from .models import Coursse

admin.site.site_header="Milson Admin Panel"
admin.site.site_title="Milson Panel"

class HideSlug(admin.ModelAdmin):
    fields='__all__'
    exclude=['slug',]

class CoursseModelAdmin(SummernoteModelAdmin):  # instead of ModelAdmin
    summernote_fields = '__all__'
   
# Register your models here.
admin.site.register(Coursse,CoursseModelAdmin)
# admin.site.register(Coursse,HideSlug)
## code to hide slug from Course table

