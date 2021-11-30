from rest_framework.response import Response
from rest_framework import status
from rest_framework.exceptions import PermissionDenied






def Success_response(msg="Request Success",data=[],status_code=status.HTTP_200_OK):

    return Response(data={
       "message":msg,
       'status_code':status_code,
       "data":data,
       "success":True
    })






class CustomError(PermissionDenied):
    'this helps me throw custom Errors Anytime AnyDay ;)'

    
    def __init__(self, message, status_code=status.HTTP_400_BAD_REQUEST):
        self.detail = {
            'message':message,
            "status_code":status_code
        }
        self.status_code =status_code