from django.shortcuts import render, get_object_or_404
from .models import Project


def all_projects(request):
    """A view to see all projects"""

    projects = Project.objects.all()

    context = {
        'projects': projects,
    }

    return render(request, 'projects/projects.html', context)


def project_detail(request, project_id):
    """A view to see all project details"""

    project = get_object_or_404(Project, pk=project_id)

    context = {
        'project': project,
    }

    return render(request, 'projects/project_detail.html', context)
