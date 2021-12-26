from django.shortcuts import render
from django.http import HttpResponse
from .models import Project

projectsList = [
        {
        'id':'1',
        'title': 'Ecommerce website',
        'description': 'fully functional ecommerce website'
        },
    {
        'id':'2',
        'title': 'portfolio  website',
        'description': 'About me'
    },
    {
        'id':'3',
        'title': 'loan management website',
        'description': 'website meant for a sacco'
    },
]

def projects(request):
    projects = Project.objects.all()
    context ={'projects': projects}
    
    return render(request, 'projects/projects.html', context)

def project(request, pk):
    projectObj = Project.objects.get(id=pk)
    tags = projectObj.tags.all()
    return render(request, 'projects/single-project.html', {'project':projectObj, 'tags':tags})
