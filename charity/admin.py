from django.contrib import admin
from charity.models import Advertisement,DonatorDonate

# Register your models here.
class DonatorDonateAdmin(admin.ModelAdmin):
    empty_value_display = '-empty-'
    list_display = ('first_name' ,'last_name')

class AdvertisementAdmin(admin.ModelAdmin):
    empty_value_display = '-empty'
    list_display = ('raiser' ,'title' ,  'description' , 'category','amount' ,'collected_amount' )
    list_filter = ('title' ,'category')
    search_fields = ['title' , 'raiser' , 'amount' , 'collected_amount']

admin.site.register(DonatorDonate , DonatorDonateAdmin)
admin.site.register(Advertisement,AdvertisementAdmin)
