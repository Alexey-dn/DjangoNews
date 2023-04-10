from allauth.account.forms import SignupForm
from django.contrib.auth.models import Group
from django.core.mail import mail_admins
from django import forms
from django.contrib.auth.models import User


class CustomSignupForm(SignupForm):
    first_name = forms.CharField(label="Имя", required=False)

    class Meta:
        model = User
        fields = (
            "first_name",
            "email",
            "password1",
            "password2",
        )

    def save(self, request):
        user = super().save(request)
        common_users = Group.objects.get(name="common users")
        user.groups.add(common_users)

        mail_admins(
            subject='Новый пользователь!',
            message=f'Пользователь {user.first_name} зарегистрировался на сайте.'
        )

        return user
