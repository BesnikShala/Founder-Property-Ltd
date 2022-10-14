from django.shortcuts import render
from projects.models import Project


def index(request):
    """ View to return index page """

    projects = Project.objects.all()

    context = {
        'projects': projects,
    }

    return render(request, 'home/index.html', context)


def error_404(request, exception=None):
    """ A view to return the 404 page """

    return render(request, 'home.404.html', status=404)


def error_500(request, exception=None):
    """ A view to return the 404 page """

    return render(request, 'home/500.html')
