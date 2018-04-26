from django import forms

class NameForm(forms.Form):
    setcourses1 = forms.CharField(label='setcourses1', max_length=4)
    """setcourses2 = forms.CharField(label='setcourses2', max_length=4)
    setcourses3 = forms.CharField(label='setcourses3', max_length=4)
    setcourses4 = forms.CharField(label='setcourses4', max_length=4)"""

class NameForm2(forms.Form):
    deletecourses = forms.CharField(label='deletecourses', max_length=4)