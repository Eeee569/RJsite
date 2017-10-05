from django.shortcuts import render
from django.template import loader
from django.http import HttpResponse
from django.http import JsonResponse
from .models import Student,Teacher,Parent

# def index(request):
#     return HttpResponse("<h1>Invalid request</h1>")
def index(request):
    template = loader.get_template('templates/html/main.html')
    return HttpResponse(template.render(None, request))

def getId(request,user_id):
    user = Student.objects.filter(id = user_id)
    data = {
        "MenueItem1":{
            "name" : "College Choice",
            "src" : "link",
            "icon" : "link"
        },
        "MenueItem2":{
            "name" : "Essays",
            "src" : "link",
            "icon" : "link"
        },
        "MenueItem3":{
            "name" : "Todo",
            "src" : "link",
            "icon" : "link"
        },
        "MenueItem4":{
            "name" : "Mail",
            "src" : "link",
            "icon" : "link"
        },
    }
    if user == None:
        user = Teacher.objects.filter(id=user_id)
        data = {
            "MenueItem1": {
                "name": "Student List",
                "src": "link",
                "icon": "link"
            },
            "MenueItem2": {
                "name": "Student Progress",
                "src": "link",
                "icon": "link"
            },
            "MenueItem3": {
                "name": "Essay edditor",
                "src": "link",
                "icon": "link"
            },
            "MenueItem4": {
                "name": "Mail",
                "src": "link",
                "icon": "link"
            },
        }
    if user == None:
        user = Parent.objects.filter(id=user_id)
        data = {
            "MenueItem1": {
                "name": "Student Progress",
                "src": "link",
                "icon": "link"
            },
            "MenueItem2": {
                "name": "Pay Bills",
                "src": "link",
                "icon": "link"
            },
            "MenueItem4": {
                "name": "Mail",
                "src": "link",
                "icon": "link"
            },
        }
    if user == None:
        data={"invalid user":"username not found"}

    return JsonResponse(data)