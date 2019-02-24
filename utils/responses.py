
from django.http import JsonResponse

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