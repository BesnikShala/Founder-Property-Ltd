from django.shortcuts import render
from django.core.mail import send_mail
from django.conf import settings
from .forms import CustomerForm


def contact(request):
    """ View to return contact page """
    if request.method == "POST":
        name = request.POST['name']
        email = request.POST['email']
        message = request.POST['message']

        send_mail(
            name,
            message,
            email,
            ['info@founderproperty.co.uk'],
            fail_silently=False,
            )
    customer_form = CustomerForm()
    template = 'contact/contact.html'
    context = {
        'customer_form': customer_form
    }


    return render(request, template, context)

