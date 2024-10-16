from django.contrib.auth.hashers import check_password, make_password
from django.core.exceptions import ValidationError
from django.forms import ModelForm, EmailField, CharField, Form

from apps.models import User


class RegistrationForm(ModelForm):
    class Meta:
        model = User
        fields = ('first_name', 'username', 'email', 'password')

    def clean_password(self):
        password = self.cleaned_data.get('password')
        return make_password(password)


class LoginForm(Form):
    email = EmailField()
    password = CharField(max_length=15)

    def clean(self):
        data = super().clean()
        email = data.get('email')
        password = data.get('password')

        self.find_user = User.objects.filter(email=email).first()
        if not self.find_user:
            raise ValidationError("Not Found account")

        if not check_password(password, self.find_user.password):
            raise ValidationError("Your wrong password")

        return data
