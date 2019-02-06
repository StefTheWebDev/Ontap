from django.contrib import admin

from .models import Reviewer, Beer, BeerInstance

# Register your models here.
admin.site.register(Reviewer)
admin.site.register(Beer)

@admin.register(BeerInstance)
class BeerInstanceAdmin(admin.ModelAdmin):
    list_display = ('beer', 'status', 'reviewer', 'review_date', 'id', 'description')
    list_filter = ('status', 'review_date')
    
    fieldsets = (
        (None, {
            'fields': ('beer', 'id')
        }),
        ('Rating', {
            'fields': ('status', 'review_date','reviewer', 'description'
		)
        }),
    )