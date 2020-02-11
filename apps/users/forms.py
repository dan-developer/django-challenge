from django.contrib.auth import get_user_model
from django.contrib.auth.forms import SetPasswordForm as DjangoSetPasswordForm, PasswordChangeForm as DjangoPasswordChangeForm, AuthenticationForm as DjangoAuthenticationForm
from django.contrib.auth.forms import UserChangeForm as DjangoUserChangeForm
from django.contrib.auth.forms import \
    UserCreationForm as DjangoUserCreationForm


class UserCreationForm(DjangoUserCreationForm):
    """
    User creation form.
    """
    class Meta(DjangoUserCreationForm.Meta):
        model = get_user_model()
        fields = ('username', 'password', 'phone')


class UserChangeForm(DjangoUserChangeForm):
    """
    Formulário de edição de usuário.
    """
    class Meta(DjangoUserChangeForm.Meta):
        model = get_user_model()
        fields = ('username', 'password', 'phone')


class SetPasswordForm(DjangoSetPasswordForm):
    pass


class PasswordChangeForm(DjangoPasswordChangeForm):
    pass


class AuthenticationForm(DjangoAuthenticationForm):
    # captcha = ReCaptchaField()
    pass