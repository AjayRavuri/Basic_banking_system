from django.contrib import admin
from Bank.models import Customer,Transaction

# Register your models here.
class CustomerAdmin(admin.ModelAdmin):
    list_display=['id','cname','accno','acctype','mail','cbal']
class TransactionAdmin(admin.ModelAdmin):
    list_display=['id','sname','saccno','rname','raccno','amnt']

admin.site.register(Customer,CustomerAdmin)
admin.site.register(Transaction,TransactionAdmin)
