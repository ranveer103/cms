
from django import forms

class SignupForm(forms.Form):
    CHOICES=[('M','Male'),
         ('F','Female')]
    CITIES = [('chd', 'Chandigarh'), ('delhi', 'Delhi'), ]     
    
    name = forms.CharField(label='Enter Name')
    email = forms.EmailField(label='Enter email')
    password = forms.CharField(label='Enter Password', widget=forms.PasswordInput())
    dob = forms.DateField(label='Enter dob', widget=forms.DateInput(attrs={'type': 'date'}))
    age = forms.IntegerField(label='Enter age')
    gender = forms.ChoiceField(choices=CHOICES,widget=forms.RadioSelect)
    city = forms.ChoiceField(choices=CITIES)
    course1 = forms.CharField(widget=forms.CheckboxInput(), label='Python')
    course2 = forms.CharField(widget=forms.CheckboxInput(), label='Java')
    #course3 = forms.CharField(widget=forms.CheckboxInput(), label='PHP')
    #field_name = forms.FileField()

    

