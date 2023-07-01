from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
from .models import Record

class SignUpForm(UserCreationForm):
    email = forms.EmailField(label="", widget=forms.TextInput(attrs={'placeholder':'Email Address', 'class':'form-control'}))
    first_name= forms.CharField(label="", max_length=50, widget=forms.TextInput(attrs={'placeholder':'First Name', 'class':'form-control'}))
    last_name =  forms.CharField(label="", max_length=50,widget=forms.TextInput(attrs={'placeholder':'Last Name', 'class':'form-control'}))
    
    class Meta:
        model = User
        fields =('username','first_name','last_name','email', 'password1','password2', )
    
    def __init__(self, *args, **kwargs):
        super(SignUpForm, self).__init__(*args,**kwargs)
        
        self.fields['username'].widget.attrs['class'] = 'form-control '
        self.fields['username'].widget.attrs['placeholder'] = 'Your User Name'
        self.fields['username'].label = ""
        self.fields['username'].help_text = "<span class='form-text text-light'><small>Required. 150 character or fewer. Letters digits and symbols.</small></span>"
        
        self.fields['password1'].widget.attrs['class'] = 'form-control'
        self.fields['password1'].widget.attrs['placeholder'] = 'Password'
        self.fields['password1'].label = ""
        self.fields['password1'].help_text = "<span class='form-text text-muted'><small>Your password must be at least 8 characters long. It must contains aty least 2 digits, 2 letters and 2 symbols</small></span>"
        
        self.fields['password2'].widget.attrs['class'] = 'form-control'
        self.fields['password2'].widget.attrs['placeholder'] = 'Password Confirmation'
        self.fields['password2'].label = ""
        self.fields['password2'].help_text ="<span class='form-text text-muted'><small>Enter the same Password</small></span>"
        

#create a record form

class AddRecordForm(forms.ModelForm):
    
    
    class Meta:
        model = Record
        fields = "__all__"
       
        exclude = ("user", )
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args,**kwargs)
        
        self.fields['first_name'].widget.attrs['class'] = 'form-control '
        self.fields['first_name'].widget.attrs['placeholder'] = ' Firt Name'
        
        self.fields['last_name'].widget.attrs['class'] = 'form-control '
        self.fields['last_name'].widget.attrs['placeholder'] = ' Last Name'
        
        self.fields['email'].widget.attrs['class'] = 'form-control '
        self.fields['email'].widget.attrs['placeholder'] = ' Email Address'
        
        self.fields['phone'].widget.attrs['class'] = 'form-control '
        self.fields['phone'].widget.attrs['placeholder'] = ' Phone Number'
        
        self.fields['address'].widget.attrs['class'] = 'form-control '
        self.fields['address'].widget.attrs['placeholder'] = ' Address'
        
        self.fields['city'].widget.attrs['class'] = 'form-control '
        self.fields['city'].widget.attrs['placeholder'] = 'The city'
        
        self.fields['state'].widget.attrs['class'] = 'form-control '
        
        self.fields['zip_code'].widget.attrs['class'] = 'form-control '
        self.fields['zip_code'].widget.attrs['placeholder'] = ' Zip Code'
        
        
    