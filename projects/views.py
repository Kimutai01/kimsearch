from django.shortcuts import render
from django.http import HttpResponse

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
    msg = 'Hello, you are on the products page'
    number = 12
    context ={'message':msg, 'number':number, 'projects': projectsList}
    
    return render(request, 'projects/projects.html', context)

def project(request, pk):
    projectObj = None
    for i in projectsList:
        if i['id'] == pk:
            projectObj = i
    return render(request, 'projects/single-project.html', {'project':projectObj})
