from django.shortcuts import render
import io
from rest_framework.parsers import JSONParser
from .serializers import StudentSerializer
from rest_framework.renderers import JSONRenderer
from django.http import HttpResponse
'''Without importing csrf_exempt it raises error, because when we create
django form, it takes csrf token by default. But in this case we have 
not created form in forms.py file, for that is why we have to import
this csrf token and apply it before defining function, as shown in line 
number 14'''  
from django.views.decorators.csrf import csrf_exempt

@csrf_exempt
def student_create(request):
    if request.method == 'POST':
        # Receive json data sent from the 3rd party application (myapp.py)
        json_data = request.body
        
        '''Convert json data into stream (that allows sending and
        receiving data)'''
        stream = io.BytesIO(json_data)
        
        # Convert stream into python data
        pythondata = JSONParser().parse(stream)
        
        '''Convert python data into model object (row) through 
        deserialization process. Because serializer is responsible for 
        both serialization and deserialization.'''
        serializer = StudentSerializer(data = pythondata)
        
        '''Check whether 'deserialized data' is suitable to be saved in 
        database or not.'''
        if serializer.is_valid():
            # Save to database.
            serializer.save()

            '''Define response message in dict format to send to the page 
            (myapp.py) from where request has been sent.'''
            response_message = {'msg':'Data created'} 
            
            # Convert response message into json data.
            json_data = JSONRenderer().render(response_message)
            '''Send response to the page (myapp.py) from where request 
            has been sent.'''
            return HttpResponse(json_data, content_type='application/json')
        
        # else block
        '''If 'serialized data' is not valid (not suitable to be saved in 
        database), it raises an error that can be accessed form 
        serializer.errors.
        Convert error message into json data and send to front end. '''
        json_data = JSONRenderer().render(serializer.errors)
        return HttpResponse(json_data, content_type='application/json')
