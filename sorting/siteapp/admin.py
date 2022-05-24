from django.contrib import admin
from siteapp.models import Sort


class SortAdmin (admin.ModelAdmin):
    list_display = [field.name for field in Sort._meta.fields]
    list_filter = ['algorithm_type']
    search_fields = ['algorithm_type', 'input_array', 'sorted_array', 'execution_time']

    class Meta:
        model = Sort


admin.site.register(Sort, SortAdmin)
