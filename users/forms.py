from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm


from .models import CustomUser, Profile


class CustomUserCreationForm(UserCreationForm):

    '''This form will allow user to register'''

    class Meta(UserCreationForm.Meta):
        model = CustomUser
        fields = ['username', 'email', 'age', 'password1']


class CustomUserChangeFrom(UserChangeForm):

    '''This form will allow superuser to register'''

    class Meta:
        model = CustomUser
        fields = UserChangeForm.Meta.fields


class UserProfileForm(forms.ModelForm):
    class Meta:
        model = CustomUser
        fields = ['username', 'email']


class UserPictureForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['image']