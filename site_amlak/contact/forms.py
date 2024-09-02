from django import forms 

class ContactForm(forms.Form):
    name=forms.CharField( max_length=50)
    email= forms.EmailField(max_length=254)
    subject=forms.CharField(max_length=50)
    content=forms.CharField(widget=forms.Textarea)