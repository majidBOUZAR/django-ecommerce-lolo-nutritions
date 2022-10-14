from django.contrib import admin
from .models import *
# Register your models here.


admin.site.site_header='Lolo Nutritions administration'
admin.site.site_title='Lolo Nutritions'
##################################################

class ContactAdmin(admin.ModelAdmin):
   def has_add_permission(self, request, obj=None):#disale button add in admin panel
        return False 
   list_display = ('phone','adress','open_time','emaill')
   list_editable = ('adress','open_time','emaill')

  



admin.site.register(Home)
admin.site.register(Contact,ContactAdmin)


