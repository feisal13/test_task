from django import forms
from allauth.account.forms import LoginForm, SignupForm, ChangePasswordForm


class MyCustomSignupForm(SignupForm):
    first_name = forms.CharField(max_length=30, label='First Name', required=False)
    last_name = forms.CharField(max_length=30, label='Last Name', required=False)
    date_of_birth = forms.DateField()

    def signup(self, request, user):
        user.first_name = self.cleaned_data['first_name']
        user.last_name = self.cleaned_data['last_name']
        user.date_of_birth = self.date_of_birth[' date of birth']
        user.safe()
        return user