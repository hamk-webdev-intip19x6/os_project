from django.contrib import admin

# Register your models here.
from .models import Creator, Type, Work, Genre, Publisher, RentedWork

class RentedWorkAdmin(admin.ModelAdmin):
    list_display = ('user', 'rented_work', 'rent_date', 'return_date', 'returned',)
    search_fields = ['rented_work__title']
    list_filter = ['rented_work__type', 'returned']

class WorkAdmin(admin.ModelAdmin):
    list_display = ('title', 'desc', 'type', 'pub_date',)
    list_filter = ['pub_date', 'type', 'publishers__publisher', 'genres__genre']
    search_fields = ['title']

admin.site.register(RentedWork, RentedWorkAdmin)
admin.site.register(Work, WorkAdmin)

admin.site.register(Creator)
admin.site.register(Type)
admin.site.register(Genre)
admin.site.register(Publisher)