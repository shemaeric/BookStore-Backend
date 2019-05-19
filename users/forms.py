from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import CustomUser
from rest_framework.permissions import IsAuthenticated

class CustomUserCreationForm(UserCreationForm):
    permission_classes = (IsAuthenticated,)

    class Meta(UserCreationForm):
        model = CustomUser
        fields = ('username', 'email')

class CustomUserChangeForm(UserChangeForm):
    permission_classes = (IsAuthenticated,)

    class Meta:
        model = CustomUser
        fields = UserChangeForm.Meta.fields