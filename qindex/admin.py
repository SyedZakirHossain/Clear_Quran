from django.contrib import admin
from.models import topic,Contact



class ServiceAdmin(admin.ModelAdmin):
    list_display=('pk','suraname','surano','verseno','verse','t_id')
admin.site.register(topic,ServiceAdmin)

class ServiceAdmin(admin.ModelAdmin):
    list_display=('pk','name','email','desc',)
admin.site.register(Contact,ServiceAdmin)



# Register your models here.
