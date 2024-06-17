from django.contrib import admin
from .models import Menu, Booking


# class MenuAdmin(admin.StackedInline):
#     model = Menu
#     extra = 3


# class MenuAdmin(admin.ModelAdmin):
#     inlines = [MenuAdmin]


# Register your models here.
admin.site.register(Menu)
admin.site.register(Booking)
