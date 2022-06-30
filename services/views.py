from django.shortcuts import render


def services(request):
    """ View to return services page """
    return render(request, 'services/services.html')
