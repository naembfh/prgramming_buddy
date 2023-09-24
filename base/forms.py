from django.forms import ModelForm
from .models import Room,UserProfile
from django import forms
class RoomForm(ModelForm):
    class Meta:
        model =Room
        fields = '__all__'
        exclude =['host','participants']



class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ['bio', 'avatar']

   
    username = forms.CharField(max_length=150, )
    email = forms.EmailField(max_length=254, )
    first_name = forms.CharField(max_length=30, )
    last_name = forms.CharField(max_length=30, )
