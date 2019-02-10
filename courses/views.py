
#Django
from django.shortcuts import render
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from django.views import View

# Models
from courses.models import Course

# Utils
import json


class coursesView(View):
    """ POST method used to save a course """
    
    @method_decorator(login_required)
    def post(self, request):
        data = json.loads(request.body.decode())
        
        courseName = data['courseName']
        if courseName == '':
            return sendError(message='Tienes que agregar un curso')

        newCourse = Course(name=courseName, teacher=request.user.teacher)
        newCourse.save()

        return sendResponse(data=data, message='Grupo agregado', code=201)
    
    
    @method_decorator(login_required)    
    def get(self, request):
        
        courses = Course.objects.filter(teacher=request.user.teacher)
        resp = []
        for course in courses:
            element = {
                'id': course.id,
                'name': course.name
            }
            resp.append(element)

        return sendResponse(data=resp)

class coursesViewId(View):

    @method_decorator(login_required)    
    def delete(self, request, *args, **kwargs):

        courseToDelete = Course.objects.get(id=kwargs['id'])

        courseDeleted = {
            'id': courseToDelete.id,
            'name': courseToDelete.name
        }

        courseToDelete.delete()
        
        return sendResponse(data=courseDeleted, message='Curso eliminado' )

def sendResponse(data, message='Success Request', code=200):
    
    response = {
        'data': data,
        'message': message,
        'code': code
    }

    return JsonResponse(response, status=code)

def sendError(message='Failed Request', code=400):
    
    response = {
        'message': message,
        'code': code
    }

    return JsonResponse(response, status=code)