# Django
from django.views import View
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required

# Local
from activities.models import Activity

#Utils
from utils.responses import sendError, sendResponse
import json

class activitiesViewApi(View):

    @method_decorator(login_required)
    def get(self, request):

        courses = Activity.objects.filter(teacher=request.user.teacher)
        resp = []
        for course in courses:
            element = {
                'id': course.id,
                'name': course.name
            }
            resp.append(element)

        return sendResponse(data=resp)


    @method_decorator(login_required)
    def post(self, request):
        data = json.loads(request.body.decode())
        
        activityName = data['activityName']
        if activityName == '':
            return sendError(message='Tienes que agregar una actividad')

        if len(activityName) > 100:
            return sendError(message='El nombre del curso es demasiado grande')

        if 'activityDesc' in data:
            activityDesc = data['activityDesc']
        else:
            activityDesc = ''

        newActivity = Activity(
            name=activityName,
            teacher=request.user.teacher,
            description=activityDesc
        )

        newActivity.save()

        data = {
            'id': newActivity.id,
            'name': newActivity.name
        }

        return sendResponse(data=data, message='Actividad {} agregada'.format(data['name']), code=201)


class activitiesViewIdApi(View):

    @method_decorator(login_required)
    def get(self, request, *args, **kwargs):

        try:
            activity = Activity.objects.get(id=kwargs['id'], teacher=request.user.teacher) 
        except expression as identifier:
            return sendError(message='La actividad no existe para este profesor', code=404)            

        activityData = {
            'id' : activity.id,
            'name' : activity.name
        }

        return sendResponse(data=activityData, message='Actividad eliminada')
    
    @method_decorator(login_required)
    def delete(self, request, *args, **kwargs):
        
        activityToDelete = Activity.objects.get(id=kwargs['id'], teacher=request.user.teacher)
        activityDeleted = {
            'id' : activityToDelete.id,
            'name' : activityToDelete.name
        }

        activityToDelete.delete()

        return sendResponse(data=activityDeleted, message='Actividad eliminada')
    
    
    @method_decorator(login_required)
    def put(self, request, *args, **kwargs):

        data = json.loads(request.body.decode())
        
        activityName = data['activityName']
        if activityName == '':
            return sendError(message='Tienes que asignarle un nombre a la actividad')

        if len(activityName) > 100:
            return sendError(message='El nombre de la activdad es demasiado grande')

        try:
            activity = Activity.objects.get(id=kwargs['id'], teacher=request.user.teacher)
        except Activity.DoesNotExist:
            return sendError(message='La actividad no existe para este profesor', code=404)
        
        # Uptade course's data
        activity.name = activityName
        activity.save()

        activityData = {
            'id': activity.id,
            'name': activity.name
        }
        
        return sendResponse(data=activityData, message='Actividad editada correctamente' )