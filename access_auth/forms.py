""" Page's Forms """

# Django
from django import forms

# Models
from django.contrib.auth.models import User

class LoginForm(forms.Form):
    """Form to validate login (email)"""

    email = forms.EmailField(
        min_length=5,
        max_length=70
    )

    password = forms.CharField(min_length=8)


class registerForm(forms.Form):
    """Form to validate a register"""

    first_name = forms.CharField(max_length=30)
    last_name = forms.CharField(max_length=30)
    middle_name = forms.CharField(max_length=30)

    email = forms.EmailField(
        min_length=5,
        max_length=70
    )

    password = forms.CharField(min_length=8)
    password_confirmation = forms.CharField(min_length=8)

    is_teacher = forms.BooleanField(required=False)

    def clean(self):

        data = super().clean()

        # Check password match
        if 'password' in data and 'password_confirmation' in data:
            password = data['password']
            password_confirmation = data['password_confirmation']
            
            if password != password_confirmation:
                msg = forms.ValidationError('No coinciden las contraseñas ')
                self.add_error('password', msg)

        # Check email is unique
        exist_user = User.objects.get(email=data['email'])
        if exist_user:
            msg = forms.ValidationError('Ya existe un usuario con éste email')
            self.add_error('email', msg)

        print('El usuario encontrado es: {}'.format(exist_user))
        
        return data

    def save(self):
        """ Save an user like teacher or student"""

        data = self.cleaned_data

