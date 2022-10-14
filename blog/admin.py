from django.contrib import admin
from .models import *

# Register your models here.
#had fclass
class CommentAdmin(admin.ModelAdmin):
   def has_add_permission(self, request, obj=None):#disale button addin admin panel
        return False 
   list_display = ('comment_mail','comment_name','comment','status')
   exclude=("comment_name","comment_mail","comment","image")#disable editable fields
   list_filter = ['status']
   list_editable: ("status")
   def get_readonly_fields(self, request, obj=None):
        if obj:
            return ["comment_name","comment_mail","comment"]
        else:
            return []

class CatAdmin(admin.ModelAdmin):
    search_fields = ['name']  


class BlogAdmin(admin.ModelAdmin):
    search_fields = ['title','description','published','category__name']               

admin.site.register(Blog,BlogAdmin)
admin.site.register(Category,CatAdmin)
admin.site.register(Comment,CommentAdmin)
