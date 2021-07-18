from django.contrib import admin

# Register your models here.
class Classlogin(admin.ModelAdmin):
    list_display=['id','username','password','email','identification']

#class ClassPages(admin.ModelAdmin):
  #  list_display=['id','page_name']

class ClassAddress(admin.ModelAdmin):
    list_display=['id','name','Company_name','Street_address','city','mobile','email']

class Classaboutinfo(admin.ModelAdmin):
    list_display=['id','basic_info','detail_info']

class ClassProduct(admin.ModelAdmin):
    list_display=['id','name','price','image','Quantity']

from .models import *
admin.site.register(log_in,Classlogin)
admin.site.register(Product, ClassProduct)
admin.site.register(EmployeeBasicInfo)
admin.site.register(EmployeeContactDetail)
admin.site.register(EmployeeSkill)
admin.site.register(EmployeeQualification)
#admin.site.register(Customer)
#admin.site.register(CustomerContact)
admin.site.register(Sell)
admin.site.register(About_us)
admin.site.register(Feedback)
admin.site.register(Fish)
#admin.site.register(Pages,ClassPages)
admin.site.register(Address,ClassAddress)
admin.site.register(About_Info,Classaboutinfo)
admin.site.register(Customers)
#admin.site.register(Req_info)
admin.site.register(OrdereProduct)

#-------combine list
class OrderItemInline(admin.TabularInline):
    model = OrdereProduct
    raw_id_fields = ['order']

@admin.register(Req_info)
class OrderAdmin(admin.ModelAdmin):
    list_display = ['id']
    #list_filter = ['paid', 'created', 'updated']
    inlines = [OrderItemInline]

@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Customers.objects.create(user=instance)