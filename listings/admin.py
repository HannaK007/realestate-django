from django.contrib import admin
from .models import Property

# Register your models here.

class PropertyAdmin(admin.ModelAdmin):
    list_display = ('title','location','price','bedrooms','bathrooms','created_at')
    prepopulated_fields = {'slug': ('title', )}
    search_fields = ('title','location','description')


admin.site.register(Property,PropertyAdmin)
