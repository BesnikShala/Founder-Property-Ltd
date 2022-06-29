from django.shortcuts import render
from .models import Project


def all_projects(request):
    """A view to see all products"""

    projects = Project.objects.all()

    context = {
        'projects': projects,
    }

    return render(request, 'projects/projects.html', context)
