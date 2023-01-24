from django import forms
from .models import *
from django.core.exceptions import ValidationError
import re
from django.contrib.auth import password_validation
from django.core.validators import RegexValidator



class SignUp (forms.ModelForm):
    moblie_number = forms.CharField(max_length=12, validators=[RegexValidator(
        '^(?:(?:\+|0{0,2})91(\s*[\ -]\s*)?|[0]?)?[789]\d{9}|(\d[ -]?){10}\d$',
        message="Enter a Valid Indian Phone Number")])
    password1 = forms.CharField(label='Password', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Password confirmation', widget=forms.PasswordInput)

    class Meta:
        model = NewUser
        fields = ('email','first_name','last_name')

    def clean_password2(self):
        # Check that the two password entries match
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")
        if password1 and password2 and password1 != password2:
            raise ValidationError("Passwords don't match")
        return password2

    def save(self, commit=True):
        # Save the provided password in hashed format
        user = super().save(commit=False)
        user.set_password(self.cleaned_data["password1"])
        if commit:
            user.save()
        return user

    def clean_password1(self):
        password1 = self.cleaned_data.get('password1')
        try:
            password_validation.validate_password(password1, self.instance)
        except forms.ValidationError as error:

            # Method inherited from BaseForm
            self.add_error('password1', error)
        return password1

class VenderForm(forms.Form):
    gst_number = forms.CharField(max_length=20, validators=[RegexValidator(
        '\d{2}[A-Z]{5}\d{4}[A-Z]{1}[A-Z\d]{1}[Z]{1}[A-Z\d]{1}', message="Enter a Valid Indian GST Number")])
    pan_number = forms.CharField(max_length=10,
                                 validators=[RegexValidator('[A-Z]{5}[0-9]{4}[A-Z]{1}',message="Enter a Valid pan number")])
    aadhar_number = forms.CharField(max_length=25, validators=[RegexValidator(
        '^[2-9]{1}[0-9]{3}\\' +'s[0-9]{4}\\s[0-9]{4}$', message="Enter a Valid Aadhar number")])
    add_line1=forms.CharField(max_length=150, validators=[RegexValidator(
        '(\d{1,}) [a-zA-Z0-9\s]+(\.)? [a-zA-Z]+(\,)? [A-Z]{2} [0-9]{5,6}', message="Enter a Valid address")])
    add_line2=forms.CharField(max_length=150, validators=[RegexValidator(
        '(\d{1,}) [a-zA-Z0-9\s]+(\.)? [a-zA-Z]+(\,)? [A-Z]{2} [0-9]{5,6}', message="Enter a Valid address")])
    pincode=forms.CharField(max_length=10,validators=[RegexValidator(
        '^[1-9]{1}[0-9]{2}\\s{0,1}[0-9]{3}$', message="Enter a Valid pincode")])
    bank_account=forms.CharField(max_length=10,validators=[RegexValidator(
        '[0-9]{9,18}', message="Enter a Valid bank account")])
    bank_name=forms.CharField(max_length=10,validators=[RegexValidator(
        '[0-9]{9,18}', message="Enter a Valid bank name")])
    #branch_name=forms.CharField(max_length=25,validators=[RegexValidator('',message='Enter a valid branch name')])
    ifsc_code=forms.CharField(max_length=15,validators=[RegexValidator('^[A-Z]{4}0[A-Z0-9]{6}$',message='Enter a valid ifsc_code')])
    upi_id=forms.CharField(max_length=15,validators=[RegexValidator('^[A-Za-z0-9.-]{2,256}@[a-zA-Z][a-zA-Z]{2,62}',message='Enter a valid upi id')])
    class Meta:
        field={'acc_name','vender_id','branch_name'}