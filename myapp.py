'''
Create a third party (client) application thorugh which client wants 
to send data. This file is made inside the project. But it is not included
it the project. we want to send request to api through this application.
By executing this application request will be sent to api.  We want to 
communicate with api through this application
client (python data converted into json) > server > (stored in) database 
(as model instance(row)). '''

import requests
import json

URL = "http://127.0.0.1:8000/stucreate/"

data = {
    'name': 'Salman',
    'roll': 1,
    'city': 'Gopalganj'
}

# convert python data into json data using dumps()
json_data = json.dumps(data)

'''Send json data to api through the url below and it returns 
a response object (response). '''
response = requests.post(url = URL, data = json_data)

# Convert response obj into json
json_data = response.json()

# Type the command 'python myapp.py' in terminal to show output.
# and Output will be shown in terminal:
# (djangoenv) PS C:\Users\pc\Desktop\deserialiization> python myapp.py
print(json_data)
