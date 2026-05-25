from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import InsuranceBrokingEntry
from .models import User
extrafields = ('image','phone')
class CustomUserAdmin(UserAdmin):
    fieldsets = UserAdmin.fieldsets + (('Other fields',{'fields':extrafields}),)
    list_display = UserAdmin.list_display + extrafields 
    list_filter = ("is_active",)

admin.site.register(User, CustomUserAdmin)
@admin.register(InsuranceBrokingEntry)
class InsuranceBrokingEntryAdmin(admin.ModelAdmin):
    list_display = [
        'policy_no', 'life_assured', 'ack_no', 'dep_name',
        'policy_amt', 'ack_date', 'ack_verified',
    ]
    list_filter = ['ack_verified', 'policy_type', 'branch_city']
    search_fields = ['policy_no', 'life_assured', 'ack_no', 'dep_name', 'application_no']
    date_hierarchy = 'ack_date'
    readonly_fields = ['created_at', 'updated_at']
    fieldsets = (
        ('Branch / Company', {
            'fields': ('company', 'branch_city', 'branch_name'),
        }),
        ('Ack Details', {
            'fields': ('policy_type', 'dep_code', 'ack_date', 'p_date', 'login_date', 'ack_no', 'ack_verified'),
        }),
        ('Staff Details', {
            'fields': (
                'staff',
                'branch_mgr',
                'branch_assist',
            ),
        }),
        ('Policy Details', {
            'fields': (
                'application_no', 'life_assured',
                'policy_no', 'policy_date', 'policy_name',
                'policy_amt', 'premium_amt', 'payment_term',
            ),
        }),
        ('Depositor Details', {
            'fields': (
                'dep_name', 'address_line1', 'address_line2', 'address_line3',
                'city', 'pin', 'mobile_number', 'phone_number',
            ),
        }),
        ('Payment Details', {
            'fields': (
                'bank', 'bank_branch', 'micr_code',
                'ifsc_code', 'check_number', 'check_amount',
            ),
        }),
        ('Nominee Details', {
            'fields': (
                'nominee_name', 'nominee_dob', 'nominee_mobile', 'nominee_email',
            ),
        }),
        ('Timestamps', {
            'fields': ('created_at', 'updated_at'),
            'classes': ('collapse',),
        }),
    )
