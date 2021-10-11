from django import forms
from .models import MyModel
 
 
# creating a form
class MyForm(forms.ModelForm):
 
    # create meta class
    class Meta:
        # specify model to be used
        model = MyModel
 
        # specify fields to be used
        fields = [
            "title",
            "description",
        ]