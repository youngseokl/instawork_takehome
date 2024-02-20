from django import forms
from .models import Member
from django.core.validators import EmailValidator, RegexValidator

class MemberForm(forms.Form):
    first_name = forms.CharField(max_length=100, 
                                 required=True,
                                 # This name validator is a bit tricky. As the name could allow special characters such as period, 
                                 # slash, apostrophe, spaces and etc. This regex pattern strictly prohibits numbers.
                                 validators=[RegexValidator(
                                    regex='^\D*$',
                                    message="Invalid First Name",
                                ),
                            ]
                        )
    last_name = forms.CharField(max_length=100, 
                                 required=True, 
                                 validators=[RegexValidator(
                                    regex='^\D*$',
                                    message="Invalid Last Name",
                                ),
                            ]
                        )
    email = forms.CharField(max_length=200, 
                            required=True, 
                            validators=[EmailValidator(message="Invalid Email")])
    phone_number = forms.CharField(max_length=100, 
                                 required=True, 
                                 validators=[RegexValidator(
                                    regex='((?:\+\d{2}[-\.\s]??|\d{4}[-\.\s]??)?(?:\d{3}[-\.\s]??\d{3}[-\.\s]??\d{4}|\(\d{3}\)\s*\d{3}[-\.\s]??\d{4}|\d{3}[-\.\s]??\d{4}))',
                                    message="Invalid Last Name",
                                ),
                            ]
                        )
    role = forms.TypedChoiceField(choices=Member.ROLE_TYPE)