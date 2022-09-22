from django.shortcuts import render
from django.core.mail import send_mail
from django.conf import settings
from .forms import CustomerForm
from django.contrib import messages


def contact(request):
    """ View to return contact page and send emails"""
    if request.method == "POST":
        customer_form = CustomerForm(request.POST)
        if customer_form.is_valid():
            name = request.POST['name']
            email = request.POST['email']
            message = request.POST['message']
            phone_number = request.POST['phone_number']
            post_code = request.POST['post_code']
            subject = 'Website Enquiry'

            message = f"Name: {name}\n\n Number: {phone_number} \n\n Email: {email} \n\n Post Code: {post_code} \n\n Message: {message}"

            email = 'info@founderproperty.co.uk'

            send_mail(
                subject,
                message,
                email,
                ['info@founderproperty.co.uk'],
                fail_silently=False,
                )
            messages.success(request, "Your email has been sent, We will get back to you as soon as possible.")
    customer_form = CustomerForm()
    template = 'contact/contact.html'
    context = {
        'customer_form': customer_form
    }

    return render(request, template, context)


