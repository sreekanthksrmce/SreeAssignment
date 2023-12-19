from django.forms import ModelForm
from .models import User

# Create the form class.
class LoginForm(ModelForm):
     class Meta:
         model = User
         fields = ['username', 'password']