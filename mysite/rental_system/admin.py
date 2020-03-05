from django.contrib import admin

# Register your models here.
from .models import Creator, Type, Work, Genre, Publisher, RentedWork

class RentedWorkAdmin(admin.ModelAdmin):
    list_display = ('user', 'rented_work', 'rent_date', 'return_date', 'date_returned', 'returned')
    search_fields = ['rented_work__title', 'user__username']
    list_filter = ['rented_work__type', 'returned']

class WorkAdmin(admin.ModelAdmin):
    list_display = ('title', 'desc', 'type', 'pub_date',)
    list_filter = ['pub_date', 'type', 'publishers__publisher', 'genres__genre']
    search_fields = ['title']
    
class CreatorAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name')
    search_fields = ['first_name', 'last_name']

admin.site.register(RentedWork, RentedWorkAdmin)
admin.site.register(Work, WorkAdmin)
admin.site.register(Creator, CreatorAdmin)

admin.site.register(Type)
admin.site.register(Genre)
admin.site.register(Publisher)