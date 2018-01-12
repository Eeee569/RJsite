from django.shortcuts import render
import json
from django.http import HttpResponse, JsonResponse
from django.core import serializers
from django.views.decorators.csrf import csrf_exempt
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from RjSite.models import Teacher,Parent,Student
from usr.serializers import StudentSerializer,ParentSerializer,TeacherSerializer

import logging, logging.config
import sys

LOGGING = {
    'version': 1,
    'handlers': {
        'console': {
            'class': 'logging.StreamHandler',
            'stream': sys.stdout,
        }
    },
    'root': {
        'handlers': ['console'],
        'level': 'INFO'
    }
}


@csrf_exempt
def robustUserhandler(request):
    logging.config.dictConfig(LOGGING)
    if request.method == 'POST':
        user_data = json.loads(request.body)
        action = user_data["action"]
        if action == 'create':
            data = JSONParser().parse(request)
            try:
                type = user_data["type"]
                if type == 's':
                    serializer = StudentSerializer(data=data)
                    if serializer.is_valid():
                        serializer.save()
                        return JsonResponse(serializer.data, status=201)
                    return JsonResponse(serializer.errors, status=400)
                elif type == 't':
                    logging.info('got to proper type: ' + type)
                    serializer = TeacherSerializer(data=data)
                    if serializer.is_valid():
                        serializer.save()
                        return JsonResponse(serializer.data, status=201)
                    return JsonResponse(serializer.errors, status=400)
                elif type == 'p':
                    serializer = ParentSerializer(data=data)
                    if serializer.is_valid():
                        serializer.save()
                        return JsonResponse(serializer.data, status=201)
                    return JsonResponse(serializer.errors, status=400)
                else:
                    raise Exception("User Type Not Possible")
            except:
                return HttpResponse(status=400)  # not sure if right error
            #return HttpResponse(status=400)  # not sure if right error



        elif action == 'find':
            try:
                type = user_data["type"]
                pk = user_data["pk"]
                if type == 's':
                    student = Student.objects.get(pk=pk)
                    serializer = StudentSerializer(student)
                    return JsonResponse(serializer.data, safe=False)
                elif type == 't':
                    teacher = Teacher.objects.get(pk=pk)
                    serializer = TeacherSerializer(teacher)
                    return JsonResponse(serializer.data, safe=False)
                elif type == 'p':
                    parent = Parent.objects.get(pk=pk)
                    serializer = ParentSerializer(parent)
                    return JsonResponse(serializer.data, safe=False)
                else:
                    raise Exception("User Type Not Possible")
            except:
                return HttpResponse(status=404)


        elif action == 'edit':
            type = user_data["type"]
            pk = user_data["pk"]
            data = JSONParser().parse(request)
            if type == 's':
                student = Student.objects.get(pk=pk)
                serializer = StudentSerializer(student)
            elif type == 't':
                teacher = Teacher.objects.get(pk=pk)
                serializer = TeacherSerializer(teacher)
            elif type == 'p':
                parent = Parent.objects.get(pk=pk)
                serializer = ParentSerializer(parent)
            if serializer.is_valid():
                serializer.save()
                return JsonResponse(serializer.data)
            return JsonResponse(serializer.errors, status=400)

        elif action == 'list':
            all_users = list(Student.objects.all()) + list(Teacher.objects.all()) + list(Parent.objects.all())
            data = serializers.serialize('json', all_users)
            return JsonResponse(data, safe=False)
        # data = JSONParser().parse(request)
        # logging.info('got data:' + str(data))
        # return JsonResponse(data,safe=False)
        #


# Create your views here.
@csrf_exempt
def index(request):#returns all users
    logging.config.dictConfig(LOGGING)
    all_users = list(Student.objects.all())+list(Teacher.objects.all())+list(Parent.objects.all())
    data = serializers.serialize('json',all_users)
    return JsonResponse(data,safe=False)

@csrf_exempt
def userViewModifyandDelete(request,pk,type):
    data = JSONParser().parse(request)
    logging.config.dictConfig(LOGGING)
    logging.info('pk:'+pk+' type:'+type)
    try:
        if type == 's':
           student=Student.objects.get(pk=pk)
        elif type == 't':
            teacher=Teacher.objects.get(pk=pk)
        elif type == 'p':
            parent=Parent.objects.get(pk=pk)
        else:
            raise Exception("User Type Not Possible")
    except:
        return HttpResponse(status=404)

    if request.method == 'GET':
        if type == 's':
            serializer = StudentSerializer(student)
            return JsonResponse(serializer.data,safe=False)
        elif type == 't':
            serializer = TeacherSerializer(teacher)
            return JsonResponse(serializer.data,safe=False)
        elif type == 'p':
            serializer = ParentSerializer(parent)
            return JsonResponse(serializer.data,safe=False)

    elif request.method == 'PUT': #may just create and not edit
        data = JSONParser().parse(request)
        if type == 's':
            serializer = StudentSerializer(student)
        elif type == 't':
            serializer = TeacherSerializer(teacher)
        elif type == 'p':
            serializer = ParentSerializer(parent)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)
        return JsonResponse(serializer.errors, status=400)

    elif request.method == 'DELETE':
        if type == 's':
            student.delete()
        elif type == 't':
            teacher.delete()
        elif type == 'p':
            parent.delete()
        return HttpResponse(status=204)
@csrf_exempt
def userCreate(request,type):
    logging.config.dictConfig(LOGGING)
    if request.method == 'POST':
        #import sys
        #print >> sys.stderr, 'Goodbye, cruel world!'
        data = JSONParser().parse(request)
        try:
            if type == 's':
                serializer = StudentSerializer(data=data)
                if serializer.is_valid():
                    serializer.save()
                    return JsonResponse(serializer.data,status=201)
                return JsonResponse(serializer.errors, status=400)
            elif type == 't':
                logging.info('got to proper type: '+type)
                serializer = TeacherSerializer(data=data)
                if serializer.is_valid():
                    serializer.save()
                    return JsonResponse(serializer.data,status=201)
                return JsonResponse(serializer.errors, status=400)
            elif type == 'p':
                serializer = ParentSerializer(data=data)
                if serializer.is_valid():
                    serializer.save()
                    return JsonResponse(serializer.data,status=201)
                return JsonResponse(serializer.errors, status=400)
            else:
                raise Exception("User Type Not Possible")
        except:
            return HttpResponse(status=400)#not sure if right error
        return HttpResponse(status=400)#not sure if right error

