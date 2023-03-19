from django import forms


class LogInForm(forms.Form):
    user_name = forms.CharField(label='user name', max_length=30)
    pwd = forms.CharField(label='password', max_length=30)


class RegisterForm(forms.Form):
    user_name = forms.CharField(label='user name', max_length=30)
    pwd = forms.CharField(label='password', max_length=30)
    first_name = forms.CharField(label='first name', max_length=30)
    last_name = forms.CharField(label='last name', max_length=30)
    email = forms.EmailField()
