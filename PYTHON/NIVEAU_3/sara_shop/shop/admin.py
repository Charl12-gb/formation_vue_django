from django.contrib import admin
from .models import Dish, Sauce, Beverage, Order

admin.site.site_header = "Tableau de Bord - SARA-SHOP"

# Register your models here.
@admin.register(Dish)
class DishAdmin(admin.ModelAdmin):
    list_display = ('name', 'formatted_price')
    search_fields = ('name',)

    def formatted_price(self, obj):
        return "${:.2f}".format(obj.price) 
    formatted_price.short_description = 'Price'

@admin.register(Sauce)
class SauceAdmin(admin.ModelAdmin):
    list_display = ('name', 'price')
    search_fields = ('name',)

@admin.register(Beverage)
class BeverageAdmin(admin.ModelAdmin):
    list_display = ('name', 'price')
    search_fields = ('name',)

class OrderAdmin(admin.ModelAdmin):
    list_display = ('id', 'customer_name', 'dish', 'sauce', 'beverage', 'calculate_total', 'processed')
    list_filter = ('processed', 'customer_name',) 
    actions = ['mark_processed', 'mark_not_processed']

    def mark_processed(self, request, queryset):
        queryset.update(processed=True)
    mark_processed.short_description = "Mark selected orders as processed"

    def mark_not_processed(self, request, queryset):
        queryset.update(processed=False)
    mark_not_processed.short_description = "Mark selected orders as not processed"

admin.site.register(Order, OrderAdmin)