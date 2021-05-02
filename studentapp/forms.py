
from django import forms


class LoginForm(forms.Form):
     user_name = forms.CharField(label= 'Enter user name', max_length=100)
     user_pass = forms.CharField(label= 'Enter Password', max_length=100 , widget=forms.PasswordInput())

     
# class SignupForm(forms.Form):
#     CHOICES=[('M','Male'),
#          ('F','Female')]
#     CITIES = [('chd', 'Chandigarh'), ('delhi', 'Delhi'), ]     
    
#     name = forms.CharField(label='Enter Name')
#     email = forms.EmailField(label='Enter email')
#     password = forms.CharField(label='Enter Password', widget=forms.PasswordInput())
#     dob = forms.DateField(label='Enter dob', widget=forms.DateInput(attrs={'type': 'date'}))
#     age = forms.IntegerField(label='Enter age')
#     gender = forms.ChoiceField(choices=CHOICES,widget=forms.RadioSelect)
#     city = forms.ChoiceField(choices=CITIES)
#     course1 = forms.CharField(widget=forms.CheckboxInput(), label='Python')
#     course2 = forms.CharField(widget=forms.CheckboxInput(), label='Java')
#     #course3 = forms.CharField(widget=forms.CheckboxInput(), label='PHP')
#     #field_name = forms.FileField()


class SignupForm(forms.Form):
#     CHOICES=[('M','Male'),
#          ('F','Female')]
#     CITIES = [('chd', 'Chandigarh'), ('delhi', 'Delhi'), ]     
    
    username = forms.CharField(label='Enter User Name')
    first_name = forms.CharField(label='Enter First Name')
    last_name = forms.CharField(label='Enter Last Name')
    email  = forms.EmailField(label='Enter Email')
    password = forms.CharField(label='Enter Password', widget=forms.PasswordInput())
#     dob = forms.DateField(label='Enter dob', widget=forms.DateInput(attrs={'type': 'date'}))
#     age = forms.IntegerField(label='Enter age')
#     gender = forms.ChoiceField(choices=CHOICES,widget=forms.RadioSelect)
#     city = forms.ChoiceField(choices=CITIES)
#     course1 = forms.CharField(widget=forms.CheckboxInput(), label='Python')
#     course2 = forms.CharField(widget=forms.CheckboxInput(), label='Java')
    #course3 = forms.CharField(widget=forms.CheckboxInput(), label='PHP')
    #field_name = forms.FileField()


    

