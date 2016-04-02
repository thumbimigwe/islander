from django import forms

from .models import SignUp


class SignUpForm(forms.ModelForm):
    class Meta:
        model = SignUp
        fields = ['full_name', 'email']
    
    
        def clean_email(self):
            email = self.cleaned_data.get('email')
            return "abc@gmail.com"
        
        def clean_full_name(self):
            full_name = self.cleaned_data.get('full_name')
            #write validation code.
            return full_name