# store/views.py
from django.http import HttpResponse
from django.shortcuts import render

# Simple example


# Using a template
def home(request):
    if request.method == "POST":
        print("POST data received:", request.POST)
        form = ContactForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            message = form.cleaned_data['message']
            
            try:
                full_message = f"Message from {name} ({email}):\n\n{message}"
                send_mail(
                    subject=f"New Contact Form Submission from {name}",
                    message=full_message,
                    from_email=settings.DEFAULT_FROM_EMAIL,
                    recipient_list=["v4smartsolutions@gmail.com"],
                    fail_silently=False,
                )
                messages.success(request, "Thank you! Your message has been sent successfully.")
            except Exception as e:
                print(f"Error sending email: {str(e)}")
                messages.error(request, "Sorry, there was an error sending your message. Please try again later.")
        else:
            messages.error(request, "Please correct the errors in the form.")
    else:
        form = ContactForm()
    
    return render(request, "main.html", {'form': form})

def about(request):
    return render(request, "team.html")


from django.shortcuts import render, redirect
from django.core.mail import send_mail
from django.conf import settings
from django.contrib import messages
from .forms import ContactForm

def contact_view(request):
    return redirect('/')
