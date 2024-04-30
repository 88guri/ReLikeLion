from django import forms
from .models import CustomUser
from django.core.exceptions import ValidationError
from django.contrib.auth import authenticate, login
from django.shortcuts import redirect, render

User = CustomUser

class LoginForm(forms.Form):
    username = forms.CharField(label='Username') 
    password = forms.CharField(label='Password', widget=forms.PasswordInput)

    def clean(self):
        cleaned_data = super().clean()
        username = cleaned_data.get('username')  
        password = cleaned_data.get('password')

        if username and password:
            user = authenticate(username=username, password=password)  
            if user is None:
                raise forms.ValidationError('Invalid username or password.')
        
        return cleaned_data

class SignUpForm(forms.ModelForm):

    class Meta:
        model = User
        fields = ('id', 'name', 'email', 'major', 'nickname', 'password', 'phone_number', 'introduction', 'hobby', 'favorite_food')
        widgets = {
            'password' : forms.PasswordInput(),
        }

    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data['password'])
        if commit:
            user.save()
        return user
 
def login_page(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)  
        if form.is_valid():
            username = form.cleaned_data['username'] 
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password) 
            if user is not None:
                # 로그인 성공
                login(request, user)
                return redirect('home')
            else:
                # 로그인 실패
                print("로그인 실패")
                pass
    else:
        form = LoginForm()  
    return render(request, 'Login.html', {'form': form})