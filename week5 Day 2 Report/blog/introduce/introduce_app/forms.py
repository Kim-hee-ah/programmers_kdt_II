from django import forms
from .models import Burger

class BurgerForm(forms.ModelForm):
    class Meta:
        model = Burger
        fields = ('id','name', 'price', 'is_set')