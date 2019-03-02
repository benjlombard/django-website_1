from django import forms
from django.core.validators import MinValueValidator, MaxValueValidator
class EmailPostForm(forms.Form):
    name = forms.CharField(max_length = 25)
    email = forms.EmailField()
    to = forms.EmailField()
    comments=  forms.CharField(required=False,widget=forms.Textarea)




class GenerateRandomUserForm(forms.Form):
    total = forms.IntegerField(
        validators=[
            MinValueValidator(50),
            MaxValueValidator(500)
        ]
    )
