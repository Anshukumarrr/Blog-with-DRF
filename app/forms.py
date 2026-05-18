from django import forms


class SignupForm(forms.Form):
   name=forms.CharField(max_length=50)
   email=forms.EmailField()
   password = forms.CharField(widget=forms.PasswordInput())
 
class loginForm(forms.Form):
   name=forms.CharField(max_length=50)
   password=forms.CharField(widget=forms.PasswordInput())
