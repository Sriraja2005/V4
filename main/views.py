from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from django.core.mail import send_mail
from django.conf import settings
from .models import ContactSubmission
from .forms import ContactForm


def home(request):
    
    
    return render(request, 'main/home.html')


def services(request):
    """Services page view"""
    services_data = [
        {
            'title': 'Software Development',
            'description': 'Custom software solutions tailored to your business needs',
            'features': [
                'Enterprise Applications',
                'API Development',
                'Database Design',
                'System Integration',
                'Performance Optimization'
            ],
            'icon': 'code'
        },
        {
            'title': 'App Development',
            'description': 'Native and cross-platform mobile applications',
            'features': [
                'iOS & Android Apps',
                'React Native',
                'Flutter Development',
                'App Store Deployment',
                'Push Notifications'
            ],
            'icon': 'smartphone'
        },
        {
            'title': 'Website Development',
            'description': 'Modern, responsive websites that drive results',
            'features': [
                'Responsive Design',
                'E-commerce Solutions',
                'CMS Integration',
                'SEO Optimization',
                'Performance Tuning'
            ],
            'icon': 'globe'
        }
    ]
    return render(request, 'main/services.html', {'services': services_data})


def about(request):
   
    return render(request, "main/about.html" )




from django.shortcuts import render, redirect
from django.core.mail import send_mail
from django.contrib import messages
from django.conf import settings
from django import forms

# ---------------------------
# CONTACT FORM (inside views.py to keep in one file)
# ---------------------------

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
            'placeholder': 'Enter the Number '
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

# ---------------------------
# CONTACT VIEW
# ---------------------------

def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data 

            # Send email notification
            send_mail(
                subject=f"📩 New Contact from {cd['name']}",
                message=f"""
You have a new contact submission:

Name: {cd['name']}
Email: {cd['email']}
Phone: {cd['phone']}
Company: {cd['company']}
Service: {cd['service_type']}

Message:
{cd['message']}
""",
                from_email=settings.DEFAULT_FROM_EMAIL,
                recipient_list=['v4smartsolutions@gmail.com'],  # 👈 change to your email
                fail_silently=False,
            )

            messages.success(request, "✅ Thank you for your message! We'll get back to you soon.")
            return redirect('contact')
    else:
        form = ContactForm()

    return render(request, 'main/contact.html', {'form': form})






# ---------- Static Portfolio Pages for Each Team Member ----------

