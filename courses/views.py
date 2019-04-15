
#Django
from django.shortcuts import render
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from django.views import View

# Models
from courses.models import Course

# Utils
import json
from utils.responses import sendError, sendResponse


class coursesViewApi(View):

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
    

    """ POST method used to save a course """
    @method_decorator(login_required)
    def post(self, request):
        
        data = json.loads(request.body.decode())
        
        courseName = data['courseName']
        if courseName == '':
            return sendError(message='Tienes que darle un nombre al curso')

        if len(courseName) > 100:
            return sendError(message='El nombre del curso es demasiado grande')

        newCourse = Course(name=courseName, teacher=request.user.teacher)
        newCourse.save()

        data = {
            'id': newCourse.id,
            'name': newCourse.name
        }

        return sendResponse(data=data, message='Grupo {} agregado'.format(data['name']), code=201)

class coursesViewIdApi(View):

    @method_decorator(login_required)    
    def delete(self, request, *args, **kwargs):

        try:
            courseToDelete = Course.objects.get(id=kwargs['id'], teacher=request.user.teacher)
        except Course.DoesNotExist:
            return sendError(message='El curso no existe para este profesor', code=404)

        courseDeleted = {
            'id': courseToDelete.id,
            'name': courseToDelete.name
        }

        courseToDelete.delete()
        
        return sendResponse(data=courseDeleted, message='Curso eliminado' )
    
    
    @method_decorator(login_required)
    def get(self, request, *args, **kwargs):

        try:
            course = Course.objects.get(id=kwargs['id'], teacher=request.user.teacher)
        except Course.DoesNotExist:
            return sendError(message='El curso no existe para este profesor', code=404)
        
        courseData = {
            'id': course.id,
            'name': course.name
        }
        
        return sendResponse(data=courseData, message='Curso mostrado' )

    
    @method_decorator(login_required)
    def put(self, request, *args, **kwargs):

        data = json.loads(request.body.decode())
        
        courseName = data['courseName']
        if courseName == '':
            return sendError(message='Tienes que darle un nombre al curso')

        if len(courseName) > 100:
            return sendError(message='El nombre del curso es demasiado grande')

        try:
            course = Course.objects.get(id=kwargs['id'], teacher=request.user.teacher)
        except Course.DoesNotExist:
            return sendError(message='El curso no existe para este profesor', code=404)
        
        # Uptade course's data
        course.name = courseName
        course.save()

        courseData = {
            'id': course.id,
            'name': course.name
        }
        
        return sendResponse(data=courseData, message='Curso editado correctamente' )

class coursesStudentsViewIdApi(View):
    
    """Get the courses's students"""
    def get(self, request, *args, **kwargs):
        
        try:
            course = Course.objects.get(id=kwargs['id'], teacher=request.user.teacher)
        except Course.DoesNotExist:
            return sendError(message='El curso no existe para este profesor', code=404)
        
        qStudents = course.students.all()

        students = []
        for student in qStudents:
            element = {
                'id': student.id,
                'status': student.status,
                'first_name': student.user.first_name,
                'last_name': student.user.last_name,
                'username': student.user.username,
                'email': student.user.email,
                'government_id': student.government_id,
            }
            students.append(element)

        return sendResponse(data=students, message='Alumnos en el curso {}'.format(course.name))