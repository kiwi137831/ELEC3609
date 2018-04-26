from django import forms
#from django.contrib.auth.models import User
from account.models import User


class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)

#The form for user to register
class UserRegistrationForm(forms.ModelForm):
    password = forms.CharField(label='Password',
                               widget=forms.PasswordInput)
    password2 = forms.CharField(label='Repeat password',
                                widget=forms.PasswordInput)
    #nick name will be showed as their preferred name and will be showed on their personal profile
    nick_name = forms.CharField(max_length=20)
    status = forms.ChoiceField(label='status',choices=[('Student','Student'),
                                                               ('Teacher','Teacher')
                                                               ])
    #university decides the courses that a user can choose to join
    #we only support three universities right now
    #you can add universities here if you want
    university = forms.ChoiceField(label='university',choices=[('USYD','USYD'),
                                                               ('UNSW','UNSW'),
                                                               ('UTS','UTS')
                                                               ])
    class Meta:
        model = User
        fields = ('username', 'email', 'university', 'status', 'nick_name', 'password')
    def clean_password2(self):
        cd = self.cleaned_data
        if cd['password'] != cd['password2']:
            raise forms.ValidationError('Passwords don\'t match.')
        return cd['password2']
