from django import forms

class StudentRegistration(forms.Form):
    name=forms.CharField(label='Your Name', label_suffix=' ', initial='Aryan', required=False , disabled=True, help_text='Limit 70 char')
   
   