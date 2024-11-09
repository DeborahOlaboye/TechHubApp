
from django.shortcuts import render, redirect
from django.core.mail import send_mail
from django.conf import settings
from contact.forms import ContactForm, QuotationForm

def homepage(request):
    return render(request, 'index.html')

def about(request):
    return render(request, 'about.html')

def testimonial(request):
    return render(request, 'testimonial.html')

def quote(request):
    form = QuotationForm(request.POST)
    if request.method == 'POST':
        if form.is_valid():
        # Get data from the form
            name = request.POST.get('name')
            email = request.POST.get('email')
            phone = request.POST.get('phone')
            budget = request.POST.get('budget')
            service = request.POST.get('floatingSelect')
            message = request.POST.get('message')

            # Construct the email content
            subject = f"New Quotation Request from {name}"
            body = (
                f"Name: {name}\n"
                f"Email: {email}\n"
                f"Phone: {phone}\n"
                f"Budget: {budget}\n"
                f"Service: {service}\n"
                f"Message: {message}"
            )

            # Send the email
            send_mail(subject, body, settings.DEFAULT_FROM_EMAIL, ['deboraholaboye@gmail.com'])

            # Redirect to a success page
            return redirect('contact_success')
        else:
            form = QuotationForm()
    return render(request, 'quote.html', {'form': form})
