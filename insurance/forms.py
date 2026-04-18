from django import forms
from .models import InsuranceBrokingEntry


class InsuranceBrokingEntryForm(forms.ModelForm):

    class Meta:
        model = InsuranceBrokingEntry
        exclude = ['created_at', 'updated_at']
        widgets = {
            # Ack Details
            'policy_type': forms.Select(attrs={'class': 'form-control'}),
            'dep_code': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'e.g. 9578202'}),
            'ack_date': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'p_date': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'login_date': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'ack_no': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'e.g. TB01055247'}),
            'ack_verified': forms.CheckboxInput(attrs={'class': 'form-check-input'}),

            # Staff Details
            'staff_code_no': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Code'}),
            'staff_code_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Staff Name'}),
            'branch_mgr_code': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Code'}),
            'branch_mgr_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Manager Name'}),
            'branch_assist_code': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Code'}),
            'branch_assist_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Assistant Name'}),
            'exec_code_no': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Code'}),
            'exec_code_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Executive Name'}),

            # Policy Details
            'application_no': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'e.g. OS19084570'}),
            'appln_date': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'life_assured': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Full Name'}),
            'policy_no': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'e.g. C5781696'}),
            'policy_date': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'policy_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Policy Product Name'}),
            'policy_amt': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': '0.00'}),
            'premium_amt': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': '0.00'}),
            'payment_term': forms.NumberInput(attrs={'class': 'form-control', 'min': 1, 'placeholder': 'Years'}),

            # Depositor Details
            'dep_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Depositor Full Name'}),
            'address_line1': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Address / Locality'}),
            'address_line2': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'PO / Village'}),
            'address_line3': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Taluk / Area'}),
            'city': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'City / District'}),
            'pin': forms.TextInput(attrs={'class': 'form-control', 'placeholder': '6-digit PIN'}),
            'mobile_number': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Mobile No.'}),
            'phone_number': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Phone No.'}),

            # Meta / Branch
            'company': forms.TextInput(attrs={'class': 'form-control'}),
            'branch_city': forms.TextInput(attrs={'class': 'form-control'}),
            'branch_name': forms.TextInput(attrs={'class': 'form-control'}),
        }

    def clean_pin(self):
        pin = self.cleaned_data.get('pin', '')
        if not pin.isdigit() or len(pin) != 6:
            raise forms.ValidationError("PIN must be exactly 6 digits.")
        return pin

    def clean_mobile_number(self):
        mob = self.cleaned_data.get('mobile_number', '')
        if mob and (not mob.isdigit() or len(mob) < 10):
            raise forms.ValidationError("Enter a valid mobile number (min 10 digits).")
        return mob