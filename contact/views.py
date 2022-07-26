from django.shortcuts import render


def contact(request):
    """ View to return contact page """
    return render(request, 'contact/contact.html')
