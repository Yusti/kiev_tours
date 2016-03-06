from django.contrib import admin

from .models import Tour, TourImage

# admin.site.register(Tour)

# admin.site.register(TourImage)

class TourImageInline(admin.TabularInline):
    model = TourImage
    extra = 0

class TourAdmin(admin.ModelAdmin):
    fieldsets = [
        (None,               {'fields': ['title']}),
        ('Tour Information', {
            'fields': ['description', 'visible', 'tourType', 'price'],
            'classes': ['collapse']}),
    ]
    inlines = [TourImageInline]

#    list_display = ('question_text', 'pub_date', 'was_published_recently')
#    list_filter = ['pub_date']
#    search_fields = ['question_text']

admin.site.register(Tour, TourAdmin)
