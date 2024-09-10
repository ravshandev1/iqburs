from django.contrib import admin
from .models import Category, Product, Thanks, Info


class ThanksAdmin(admin.TabularInline):
    model = Thanks
    extra = 0

class InfoAdmin(admin.TabularInline):
    model = Info
    extra = 0


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    inlines = [InfoAdmin, ThanksAdmin]


admin.site.register([Category])
