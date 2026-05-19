from django import forms
from .models import InsuranceBrokingEntry


class InsuranceBrokingEntryForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        user_queryset = self.fields['staff'].queryset.order_by('first_name', 'last_name', 'username')
        for field_name in ['staff', 'branch_mgr', 'branch_assist']:
            self.fields[field_name].queryset = user_queryset
            self.fields[field_name].empty_label = 'Select user'
            self.fields[field_name].label_from_instance = self.user_label_from_instance

    @staticmethod
    def user_label_from_instance(user):
        name_parts = [part for part in [user.first_name, user.last_name] if part]
        full_name = " ".join(name_parts)
        if full_name and user.username:
            return f"{full_name} ({user.username})"
        if user.first_name and user.username:
            return f"{user.first_name} ({user.username})"
        return full_name or user.username

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
            'staff': forms.Select(attrs={'class': 'form-select'}),
            'branch_mgr': forms.Select(attrs={'class': 'form-select'}),
            'branch_assist': forms.Select(attrs={'class': 'form-select'}),

            # Policy Details
            'application_no': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'e.g. OS19084570'}),
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

            # Nominee Details
            'nominee_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Nominee Full Name'}),
            'nominee_dob': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'nominee_email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'nominee@email.com'}),
            'nominee_mobile': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Mobile No.'}),

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

    def clean_nominee_mobile(self):
        mob = self.cleaned_data.get('nominee_mobile', '')
        if mob and (not mob.isdigit() or len(mob) < 10):
            raise forms.ValidationError("Enter a valid mobile number (min 10 digits).")
        return mob
