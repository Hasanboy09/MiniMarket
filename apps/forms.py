from django.contrib.auth.hashers import check_password, make_password
from django.core.exceptions import ValidationError
from django.db.models import ImageField
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


class ProfileEditForm(Form):
    first_name = CharField(max_length=255)
    last_name = CharField(max_length=255)
    email = CharField(max_length=255)
    phone = CharField(max_length=12)
    mobile = CharField(max_length=12)
    image = ImageField(upload_to='profile')
    skype_number = CharField(max_length=255)
