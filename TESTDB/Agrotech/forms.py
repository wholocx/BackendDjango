from django.contrib.auth.forms import UserCreationForm, forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import PasswordChangeForm
from django.core.exceptions import ValidationError
from django.contrib.auth import authenticate, get_user_model, password_validation

class CreateUserForm(UserCreationForm):
    error_css_class = 'form_error'

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
    
    def __init__(self, *args, **kwargs):
        super(CreateUserForm, self).__init__(*args, **kwargs)
        self.fields['username'].widget.attrs.update({'class': 'form_input'})
        self.fields['email'].widget.attrs.update({'class': 'form_input'})
        self.fields['password1'].widget.attrs.update({'class': 'form_input'})
        self.fields['password2'].widget.attrs.update({'class': 'form_input'})


class PasswordChangerForm(forms.Form):
    
    old_password = forms.CharField(widget = forms.PasswordInput(attrs = {'class': 'record__pass_input', 'placeholder': 'Старый пароль'}))
    new_password1 = forms.CharField(widget = forms.PasswordInput(attrs = {'class': 'record__pass_input', 'placeholder': 'Новый пароль'}))
    new_password2 = forms.CharField(widget = forms.PasswordInput(attrs = {'class': 'record__pass_input', 'placeholder': 'Повторите пароль'}))

    class Meta:
        model = User
        fields = ['old_password', 'new_password1', 'new_password2']
    
    def clean(self):
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")
        if password1 and password2 and password1 != password2:
            raise ValidationError(
                self.error_messages["password_mismatch"],
                code="password_mismatch",
            )
        password_validation.validate_password(password2, self.user)
        return password2