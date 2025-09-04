from django import forms

class ContactForm(forms.Form):
    name = forms.CharField(max_length=100)
    email = forms.EmailField()
    phone = forms.CharField(max_length=20, required=False)
    company = forms.CharField(max_length=100, required=False)
    service_type = forms.CharField(max_length=100, required=False)
    budget_range = forms.CharField(max_length=50, required=False)
    message = forms.CharField(widget=forms.Textarea)
