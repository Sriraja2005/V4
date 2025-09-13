from django import forms

SERVICE_CHOICES = [
    ('software', 'Software Development'),
    ('app', 'App Development'),
    ('web', 'Website Development'),
    ('uiux', 'UI/UX Design'),
]

class ContactForm(forms.Form):
    name = forms.CharField(
        label="Full Name",
        widget=forms.TextInput(attrs={
            'class': 'w-full border border-gray-300 rounded-lg p-3 focus:ring-2 focus:ring-blue-500 focus:outline-none',
            'placeholder': 'Your full name'
        })
    )
    email = forms.EmailField(
        label="Email Address",
        widget=forms.EmailInput(attrs={
            'class': 'w-full border border-gray-300 rounded-lg p-3 focus:ring-2 focus:ring-blue-500 focus:outline-none',
            'placeholder': 'your@email.com'
        })
    )
    phone = forms.CharField(
        label="Phone Number",
        required=False,
        widget=forms.TextInput(attrs={
            'class': 'w-full border border-gray-300 rounded-lg p-3 focus:ring-2 focus:ring-blue-500 focus:outline-none',
            'placeholder': 'Optional'
        })
    )
    company = forms.CharField(
        label="Company Name",
        required=False,
        widget=forms.TextInput(attrs={
            'class': 'w-full border border-gray-300 rounded-lg p-3 focus:ring-2 focus:ring-blue-500 focus:outline-none',
            'placeholder': 'Your company'
        })
    )
    service_type = forms.ChoiceField(
        choices=SERVICE_CHOICES,
        label="Service Needed",
        widget=forms.Select(attrs={
            'class': 'w-full border border-gray-300 rounded-lg p-3 focus:ring-2 focus:ring-blue-500 focus:outline-none',
        })
    )
    message = forms.CharField(
        label="Project Details",
        widget=forms.Textarea(attrs={
            'class': 'w-full border border-gray-300 rounded-lg p-3 focus:ring-2 focus:ring-blue-500 focus:outline-none',
            'rows': 4,
            'placeholder': 'Tell us about your project...'
        })
    )
