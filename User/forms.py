from django import forms
from django.contrib.auth import authenticate
from django.contrib.auth.forms import UserCreationForm
from .models import User

roles = (
    ('student', "Student"),
    ('Instructor', "Instructor"),
)

Gender = (
    ('M', "Male"),
    ('F', "Female"),
)

class StudentRegistrationForm(UserCreationForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['gender'].required = True
        self.fields['first_name'].label = "First Name :"
        self.fields['last_name'].label = "Last Name :"
        self.fields['password1'].label = "Password :"
        self.fields['password2'].label = "Confirm Password :"
        self.fields['email'].label = "Email :"
        self.fields['gender'].label = "Gender :"

        self.fields['first_name'].widget.attrs.update(
            {
                'placeholder': 'Enter First Name',
            }
        )
        self.fields['last_name'].widget.attrs.update(
            {
                'placeholder': 'Enter Last Name',
            }
        )
        self.fields['email'].widget.attrs.update(
            {
                'placeholder': 'Enter Email',
            }
        )
        self.fields['password1'].widget.attrs.update(
            {
                'placeholder': 'Enter Password',
            }
        )
        self.fields['password2'].widget.attrs.update(
            {
                'placeholder': 'Confirm Password',
            }
        )

    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email', 'password1', 'password2', 'gender']

    def clean_gender(self):
        gender = self.cleaned_data.get('gender')
        if not gender:
            raise forms.ValidationError("Gender is required")
        return gender

    def save(self, commit=True):
        user = super().save(commit=False)
        user.role = "Student"
        if commit:
            user.save()
        return user


class UserLoginForm(forms.Form):
    email = forms.EmailField(widget=forms.EmailInput(attrs={'placeholder': 'Email'}))
    password = forms.CharField(strip=False, widget=forms.PasswordInput(attrs={'placeholder': 'Password'}))

    def clean(self, *args, **kwargs):
        email = self.cleaned_data.get("email")
        password = self.cleaned_data.get("password")

        if email and password:
            self.user = authenticate(email=email, password=password)
            if self.user is None:
                raise forms.ValidationError("Invalid email or password.")
            if not self.user.is_active:
                raise forms.ValidationError("This account is inactive.")

        return super().clean(*args, **kwargs)
    
    def get_user(self):
        return self.user

class InstructorRegistrationForm(UserCreationForm):
    bio = forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control', 'rows': 5}), required=True)
    profile_picture = forms.ImageField(required=True, widget=forms.FileInput(attrs={'class': 'form-control'}))
    facebook = forms.URLField(max_length=200, required=False, widget=forms.URLInput(attrs={'class': 'form-control'}))
    twitter = forms.URLField(max_length=200, required=False, widget=forms.URLInput(attrs={'class': 'form-control'}))
    linkedin = forms.URLField(max_length=200, required=False, widget=forms.URLInput(attrs={'class': 'form-control'}))
    instagram = forms.URLField(max_length=200, required=False, widget=forms.URLInput(attrs={'class': 'form-control'}))

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['gender'].required = True
        self.fields['first_name'].label = "First Name :"
        self.fields['last_name'].label = "Last Name :"
        self.fields['password1'].label = "Password :"
        self.fields['password2'].label = "Confirm Password :"
        self.fields['email'].label = "Email :"
        self.fields['gender'].label = "Gender :"

        self.fields['first_name'].widget.attrs.update({'placeholder': 'Enter First Name'})
        self.fields['last_name'].widget.attrs.update({'placeholder': 'Enter Last Name'})
        self.fields['email'].widget.attrs.update({'placeholder': 'Enter Email'})
        self.fields['password1'].widget.attrs.update({'placeholder': 'Enter Password'})
        self.fields['password2'].widget.attrs.update({'placeholder': 'Confirm Password'})

    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email', 'password1', 'password2', 'gender', 'bio', 'profile_picture', 'facebook', 'twitter', 'linkedin', 'instagram']

    def clean_gender(self):
        gender = self.cleaned_data.get('gender')
        if not gender:
            raise forms.ValidationError("Gender is required")
        return gender

    def save(self, commit=True):
        user = super().save(commit=False)
        user.role = "Instructor"
        if commit:
            user.save()
        return user


class StudentProfileEditForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['first_name'].widget.attrs.update({'placeholder': 'Enter First Name'})
        self.fields['last_name'].widget.attrs.update({'placeholder': 'Enter Last Name'})

    class Meta:
        model = User
        fields = ["first_name", "last_name", "gender"]


class UserProfileForm(forms.ModelForm):
    class Meta:
        model = User
        fields = [
            'first_name', 
            'last_name', 
            'email', 
            'profile_picture', 
            
        ]
        widgets = {
            'first_name': forms.TextInput(attrs={'required': False}),
            'last_name': forms.TextInput(attrs={'required': False}),
            'email': forms.EmailInput(attrs={'required': False}),
            'profile_picture': forms.ClearableFileInput(attrs={'required': False}),
            
        }

class InstructorProfileForm(forms.ModelForm):
    class Meta:
        model = User
        fields = [
            'first_name',
            'last_name',
            'bio',
            'email',
            'profile_picture',
            'facebook',
            'instagram',
            'linkedin',
            'twitter',
        ]

    def __init__(self, *args, **kwargs):
        super(InstructorProfileForm, self).__init__(*args, **kwargs)
        for _, field in self.fields.items():
            if field.widget.__class__.__name__ != 'FileInput':
                field.widget.attrs.update({'class': 'form-control'})
            else:
                field.widget.attrs.update({'class': 'form-control-file'})