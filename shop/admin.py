from django.contrib import admin
from shop.models import *

# Register your models here.

######################################################################################

class ProductAdmin(admin.ModelAdmin):
   search_fields = ['title','price','quantity1','category','discounted_price','description','shortinfo']
   list_display = ('title','price','quantity1','category')
   list_filter = ('quantity1','weight','category')



######################################################################################


class CustomAdmin(admin.ModelAdmin):
   def has_add_permission(self, request, obj=None):#disale button addin admin panel
        return False 
   list_display = ('user','name','email')
   search_fields = ['user__username','name','email']
   exclude=("user","name","email")#disable editable fields
   def get_readonly_fields(self, request, obj=None):
        if obj:
            return ["user","name","email"]
        else:
            return []
######################################################################################
class OrderItemAdmin(admin.ModelAdmin):
   def has_add_permission(self, request, obj=None):#disale button addin admin panel
        return False 
   list_display = ('product','order','quantity')
   search_fields = ['product__title']
   list_filter = ['order__complete']
   exclude=("product","order","quantity")#disable editable fields
   def get_readonly_fields(self, request, obj=None):
        if obj:
            return ["product","order","quantity"]
        else:
            return []  
######################################################################################
class OrderAdmin(admin.ModelAdmin):
   def has_add_permission(self, request, obj=None):#disale button addin admin panel
        return False 
   list_display = ('customer','date_ordered','complete','transaction_id')
   list_editable = ['complete']
   search_fields = ['date_ordered','customer__name','transaction_id']
   list_filter = ['complete']
   exclude=("customer","date_ordered")#disable editable fields
   def get_readonly_fields(self, request, obj=None):
        if obj:
            return ["customer","date_ordered"]
        else:
            return []              


######################################################################################
class ShippingAdmin(admin.ModelAdmin):
   def has_add_permission(self, request, obj=None):#disale button addin admin panel
        return False 
   list_display = ('customer','address','phone_number')
   search_fields = ['customer__name','address','phone_number']
   #list_filter = ['order']
   exclude=('customer','order','address','phone_number','city','postal_code','country')#disable editable fields
   def get_readonly_fields(self, request, obj=None):
        if obj:
            return ('customer','order','address','phone_number','city','postal_code','country')
        else:
            return []  



admin.site.register(Product,ProductAdmin)
admin.site.register(Customer,CustomAdmin)
admin.site.register(Order,OrderAdmin)
admin.site.register(OrderItem,OrderItemAdmin)
admin.site.register(ShippingAddress,ShippingAdmin)

