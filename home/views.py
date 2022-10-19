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
    """ A view to return the 404 error page """

    return render(request, '404.html', status=404)


def error_500(request, *args, **argv):
    """ A view to return the 500 error page """

    return render(request, '500.html', status=500)
