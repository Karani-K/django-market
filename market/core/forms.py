from django import forms
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth.models  import User

class SignUpForm (UserCreationForm):
    # username=forms.CharField(max_length=50, required=True)
    # email=forms.EmailField(widget=forms.EmailInput(attrs={'class':'relative'}))  
    # password1=forms.CharField( label= "Password")
    # password2=forms.CharField(label='Confirm Password')
    class Meta:
        model= User
        fields=  ('username', 'email', 'password1', 'password2')
        # Custom authentication form to add a custom field 
        username= forms.CharField(widget=forms.TextInput(attrs={
            'placeholder': 'Username', 
            # 'class':'px-2 py-3 mt-1 block w-full rounded-md border border-gray-300 shadow-sm focus:border-sky-500 focus:outline-none focus:ring-sky-500 sm:text-sm'
        }) )    
        email= forms.CharField(widget=forms.EmailInput(attrs={
            'placeholder': 'Your Email address', 
            'class':'px-2 py-3 mt-1 block w-full rounded-md border border-gray-300 shadow-sm focus:border-sky-500 focus:outline-none focus:ring-sky-500 sm:text-sm'
        }) )
        password1= forms.CharField(widget=forms.PasswordInput(attrs={
            'placeholder': 'password', 
            'class':'px-2 py-3 mt-1 block w-full rounded-md border border-gray-300 shadow-sm focus:border-sky-500 focus:outline-none focus:ring-sky-500 sm:text-sm'
        }) )     
        password2= forms.CharField(widget=forms.PasswordInput(attrs={
            'placeholder': 'confirm password', 
            'class':'px-2 py-3 mt-1 block w-full rounded-md border border-gray-300 shadow-sm focus:border-sky-500 focus:outline-none focus:ring-sky-500 sm:text-sm'
        }) )      

class LoginForm(AuthenticationForm):
    class Meta:
        model = User 
        fields = ['username','password']
        # Adding CSS classes to the login page
        username= forms.CharField(widget=forms.TextInput(attrs={
            'placeholder': 'Username', 
            'class':'border border-solid-slate-300 w-full px-6 py-4 rounded-xl'
        }) )
        password= forms.CharField(widget=forms.PasswordInput(attrs={
            'placeholder': 'Enter Password', 
            'class':'w-full px-6 py-4 rounded-xl'
        }) )
