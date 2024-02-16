from django import forms
from .models import Member

class MemberForm(forms.Form):
    first_name = forms.CharField(max_length=100)
    last_name = forms.CharField(max_length=100)
    email = forms.CharField(max_length=200)
    phone_number = forms.CharField(max_length=100)
    status = forms.TypedChoiceField(choices=Member.ROLE_TYPE)