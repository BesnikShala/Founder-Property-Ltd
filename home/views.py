from django.shortcuts import render
from projects.models import Project


def index(request):
    """ View to return index page """

    projects = Project.objects.all()

    context = {
        'projects': projects,
    }

    return render(request, 'home/index.html', context)



def all_projects(request):
    """A view to see all projects"""

    projects = Project.objects.all()

    context = {
        'projects': projects,
    }

    return render(request, 'projects/projects.html', context)
