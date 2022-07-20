from django.contrib.auth.forms import AuthenticationForm, UserCreationForm, UserChangeForm
from django.forms import forms, HiddenInput

from auth_app.models import SchoolUser


class SchoolUserLoginForm(AuthenticationForm):

    class Meta:
        model = SchoolUser
        fields = ('username', 'password',)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'


class SchoolUserRegisterForm(UserCreationForm):

    class Meta:
        model = SchoolUser
        fields = ('username', 'first_name', 'email', 'age', 'password1', 'password2')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'


class SchoolUserEditForm(UserChangeForm):
    class Meta:
        model = SchoolUser
        fields = ('username', 'first_name', 'last_name', 'email', 'age', 'password', 'avatar')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'
            if field_name == 'password':  # Это можно использовать при восстановлении паролья
                field.widget = HiddenInput()

    def clean_age(self):
        data_age = self.cleaned_data['age']
        if data_age < 18:
            raise forms.ValidationError('Вы слишком маленький')

        return data_age


