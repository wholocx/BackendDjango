from django.contrib.auth.forms import UserCreationForm, forms
from django.contrib.auth.models import User



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
