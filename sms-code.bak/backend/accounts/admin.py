from django.contrib import admin
from tabbed_admin import TabbedModelAdmin
from .models import AccountUser, City, Account


# Register your models here.

@admin.register(City)
class CityAdmin(admin.ModelAdmin):
    search_fields = ['id','name']


class AccountUserInline(admin.StackedInline):
    model = AccountUser
    extra = 0
    fieldsets = (
        ("User", {'fields': ('name' , 'title', 'password', 'partition' , 'in_out_codes')}),
        ("Contact", {'fields': ( 'phone_number1', 'phone_number2', 'phone_number3',)}),
        
        ("Control", {'fields': ( 'holiday_begins', 'holiday_ends', 'keypad_code', 'hot_user',
                                'authorized_days_sat', 'authorized_days_sun', 'authorized_days_mon',
                                'authorized_days_tue', 'authorized_days_wed', 'authorized_days_thu',
                                'authorized_days_fri',)}),

    )
       
       
@admin.register(Account)
class AccountAdmin(TabbedModelAdmin):
    list_display = ('id', 'name', 'city', 'created_at', 'updated_at', 'created_by')
    search_fields = ['id','name', 'email', 'phone_number1', 'phone_number2' , 'phone_number3', 'whatsapp_number']
    list_filter = ['city']
    
    basic_tab = (
        ("Account", {'fields': ( 'id','name', 'address_line1', 'address_line2', 'address_line3', 'city', 'zip_code',)}),
        ("Contact", {'fields': ( 'email', 'phone_number1', 'phone_number2', 'whatsapp_number',)}),
    )
    misc_tab = (
        (None, {'fields': ( 'security_number', 'memo',
                    'police_number1', 'police_number2', 'police_number3', 
                    'fire_dept_number1','fire_dept_number2', 'fire_dept_number3',
                    'emergency_number1', 'emergency_number2','emergency_number3',)}),
                    
    )      
    partition_tab = (
         (None, {'fields': ( 'partition_name1', 'partition_name2', 'partition_name3',
                    'partition_name4', 'partition_name5', 'partition_name6', 'partition_name7', 'partition_name8',
                    'partition_name9', 'partition_name10',)}),
   
    )
    
    users_tab = (AccountUserInline,)
    
    tabs = [
        ("Basic", basic_tab),
        ("Misc", misc_tab),
        ("Partitions", partition_tab),
        ("Users", users_tab),
    ]
    
    def save_model(self, request, obj, form, change):
        if not obj.created_by:
            obj.created_by = request.user
        obj.save()
        

    
