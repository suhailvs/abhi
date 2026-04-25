from django.db import models


class InsuranceBrokingEntry(models.Model):
    POLICY_TYPE_CHOICES = [
        ('active_normal', 'Active - Normal Policy Cleared'),
        ('inactive', 'Inactive'),
        ('lapsed', 'Lapsed'),
    ]

    # Ack Details
    policy_type = models.CharField(max_length=50, choices=POLICY_TYPE_CHOICES, default='active_normal')
    dep_code = models.CharField(max_length=20, verbose_name="Dep. Code")
    ack_date = models.DateField(verbose_name="Ack Date")
    p_date = models.DateField(verbose_name="PDate")
    login_date = models.DateField(verbose_name="Login Date")
    ack_no = models.CharField(max_length=50, verbose_name="Ack No.")
    ack_verified = models.BooleanField(default=False, verbose_name="Ack is Verified")

    # Staff Details
    staff_code_no = models.CharField(max_length=10, verbose_name="Staff Code No", blank=True)
    staff_code_name = models.CharField(max_length=100, verbose_name="Staff Name")
    branch_mgr_code = models.CharField(max_length=10, verbose_name="Branch Mgr Code", blank=True)
    branch_mgr_name = models.CharField(max_length=100, verbose_name="Branch Manager")
    branch_assist_code = models.CharField(max_length=10, verbose_name="Branch Assist Code", blank=True)
    branch_assist_name = models.CharField(max_length=100, verbose_name="Branch Assistant")
    exec_code_no = models.CharField(max_length=10, verbose_name="Exec. Code No", blank=True)
    exec_code_name = models.CharField(max_length=100, verbose_name="Executive Name")

    # Policy Details
    application_no = models.CharField(max_length=30, verbose_name="Application No")
    appln_date = models.DateField(verbose_name="Application Date")
    life_assured = models.CharField(max_length=100, verbose_name="Life Assured")
    policy_no = models.CharField(max_length=30, unique=True, verbose_name="Policy No.")
    policy_date = models.DateField(verbose_name="Policy Date")
    policy_name = models.CharField(max_length=200, verbose_name="Policy Name")
    policy_amt = models.DecimalField(max_digits=12, decimal_places=2, verbose_name="Policy Amount")
    premium_amt = models.DecimalField(max_digits=12, decimal_places=2, verbose_name="Premium Amount")
    payment_term = models.PositiveIntegerField(verbose_name="Payment Term (Years)")

    # Depositor Details
    dep_name = models.CharField(max_length=100, verbose_name="Depositor Name")
    address_line1 = models.CharField(max_length=200, verbose_name="Address Line 1")
    address_line2 = models.CharField(max_length=200, blank=True, verbose_name="Address Line 2 (PO)")
    address_line3 = models.CharField(max_length=200, blank=True, verbose_name="Address Line 3")
    city = models.CharField(max_length=100, verbose_name="City")
    pin = models.CharField(max_length=10, verbose_name="PIN Code")
    mobile_number = models.CharField(max_length=15, blank=True, verbose_name="Mobile Number")
    phone_number = models.CharField(max_length=15, blank=True, verbose_name="Phone Number")

    # Nominee Details
    nominee_name = models.CharField(max_length=100, verbose_name="Nominee Name")
    nominee_dob = models.DateField(verbose_name="Nominee Date of Birth")
    nominee_email = models.EmailField(max_length=200, blank=True, verbose_name="Nominee Email ID")
    nominee_mobile = models.CharField(max_length=15, verbose_name="Nominee Mobile Number")

    # Meta
    company = models.CharField(max_length=200, default="ICICI PRUDENTIAL LIFE INSURANCE COMPANY LIMITED")
    branch_city = models.CharField(max_length=100, default="KODUNGALLUR", verbose_name="City")
    branch_name = models.CharField(max_length=100, default="KODUNGALLUR", verbose_name="Branch")

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "Insurance Broking Entry"
        verbose_name_plural = "Insurance Broking Entries"
        ordering = ['-created_at']

    def __str__(self):
        return f"{self.policy_no} - {self.life_assured}"