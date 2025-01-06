from django import forms
from .models import CustomUser

class ExampleForm(forms.ModelForm):
    class Meta:
        model = CustomUser
        fields = ['email', 'username', 'date_of_birth', 'profile_photo', 'password']

    def __init__(self, *args, **kwargs):
        super(ExampleForm, self).__init__(*args, **kwargs)
        self.fields['password'].widget = forms.PasswordInput()