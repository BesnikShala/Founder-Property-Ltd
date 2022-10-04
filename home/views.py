from django.shortcuts import render
from projects.models import Project


def index(request):
    """ View to return index page """

    projects = Project.objects.all()

    context = {
        'projects': projects,
    }

    return render(request, 'home/index.html', context)


def error_404(request, exception):
    """ A view to return the 404 page """

    return render(request, '404.html')
