from django.contrib import admin
from .models import InsuranceBrokingEntry


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
                ('staff_code_no', 'staff_code_name'),
                ('branch_mgr_code', 'branch_mgr_name'),
                ('branch_assist_code', 'branch_assist_name'),
                ('exec_code_no', 'exec_code_name'),
            ),
        }),
        ('Policy Details', {
            'fields': (
                'application_no', 'appln_date', 'life_assured',
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