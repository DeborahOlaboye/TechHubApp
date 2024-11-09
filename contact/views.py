# views.py
from django.core.mail import send_mail
from django.shortcuts import render, redirect
from django.conf import settings
from .forms import ContactForm, QuotationForm

def contact_view(request):
    form = ContactForm(request.POST)
    if request.method == 'POST':
        if form.is_valid():
            name = request.POST.get('name')
            email = request.POST.get('email')
            phone = request.POST.get('phone')
            message = request.POST.get('message')

            # Construct the email content
            subject = f"New Contact Form Submission from {name}"
            body = (
                f"Name: {name}\n"
                f"Email: {email}\n"
                f"Phone: {phone}\n"
                f"Message: {message}"
            )
            send_mail(subject, body, settings.DEFAULT_FROM_EMAIL, ['deboraholaboye@gmail.com'])

            # Redirect to a success page
            return redirect('contact_success')
        else:
            form = ContactForm()
    return render(request, 'contact.html', {'form': form})


def contact_success(request):
    return render(request, 'contact_success.html')

def quote(request):
    form = QuotationForm(request.POST)
    if request.method == 'POST':
        if form.is_valid():
        # Get data from the form
            name = request.POST.get('name')
            email = request.POST.get('email')
            phone = request.POST.get('phone')
            message = request.POST.get('message')

            # Construct the email content
            subject = f"New Contact Form Submission from {name}"
            body = (
                f"Name: {name}\n"
                f"Email: {email}\n"
                f"Phone: {phone}\n"
                f"Message: {message}"
            )

            # Send the email
            
