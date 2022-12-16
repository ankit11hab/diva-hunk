from django import forms
from .models import Voter

class VoterRegisterForm(forms.ModelForm):
    email = forms.EmailField()
    class Meta:
        model = Voter
        fields = ['name','contact','email','otp']