# LibraryProject/bookshelf/forms.py
from django import forms

class ExampleForm(forms.Form):
    # Define your form fields here
    name = forms.CharField(max_length=255)
    email = forms.EmailField()

