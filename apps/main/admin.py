from django.contrib import admin
from .models import About, Feedback, Certificate, Carousel, Application, Advantage


@admin.register(Application)
class ApplicationAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'phone', 'is_read', 'created_at')
    list_filter = ('is_read', 'created_at')
@admin.register(Advantage)
class AdvantageAdmin(admin.ModelAdmin):
    list_display = ['heading']

admin.site.register([About, Feedback, Certificate, Carousel])
