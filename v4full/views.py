# store/views.py
from django.http import HttpResponse
from django.shortcuts import render

# Simple example


# Using a template
def home(request):
    if request.method == "POST":
        # Print the POST data for debugging
        print("POST data received in home view:", request.POST)
        
        form = ContactForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            message = form.cleaned_data['message']
            
            print(f"Form is valid. Name: {name}, Email: {email}, Message: {message}")

            try:
                # Attempt to send email
                full_message = f"Message from {name} ({email}):\n\n{message}"
                send_mail(
                    subject=f"New Contact Form Submission from {name}",
                    message=full_message,
                    from_email=settings.DEFAULT_FROM_EMAIL,
                    recipient_list=["v4smartsolutions@gmail.com"],
                    fail_silently=False,
                )
                print("Email sent successfully!")
               
            except Exception as e:
                print(f"Error sending email: {str(e)}")
                messages.error(request, "Sorry, there was an error sending your message. Please try again later.")
        else:
            print("Form is invalid:", form.errors)
           
    return render(request, "main.html", {'form': ContactForm()})

def about(request):
    return render(request, "team.html")


from django.shortcuts import render, redirect
from django.core.mail import send_mail
from django.conf import settings
from django.contrib import messages
from .forms import ContactForm

def contact_view(request):
    if request.method == "POST":
        # Print the POST data for debugging
        print("POST data received:", request.POST)
        
        form = ContactForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            message = form.cleaned_data['message']
            
            print(f"Form is valid. Name: {name}, Email: {email}, Message: {message}")

            try:
                # Attempt to send email
                full_message = f"Message from {name} ({email}):\n\n{message}"
                send_mail(
                    subject=f"New Contact Form Submission from {name}",
                    message=full_message,
                    from_email=settings.DEFAULT_FROM_EMAIL,
                    recipient_list=["v4smartsolutions@gmail.com"],
                    fail_silently=False,
                )
                print("Email sent successfully!")
                
            except Exception as e:
                print(f"Error sending email: {str(e)}")
                messages.error(request, "Sorry, there was an error sending your message. Please try again later.")
        else:
            print("Form is invalid:", form.errors)
            
    
    return render(request, 'main.html', {'form': form if request.method == "POST" else ContactForm()})
