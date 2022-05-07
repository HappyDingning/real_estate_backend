from django.contrib import admin

from token_info.models import BucketInfo, RealEstateBaseInfo

class BucketInfoAdmin(admin.ModelAdmin):
    list_display = ('name', 'end_point', 'file_type')

class RealEstateBaseInfoAdmin(admin.ModelAdmin):
    list_display = ('creator', 'name', 'description')

admin.site.register(BucketInfo, BucketInfoAdmin)
admin.site.register(RealEstateBaseInfo, RealEstateBaseInfoAdmin)
