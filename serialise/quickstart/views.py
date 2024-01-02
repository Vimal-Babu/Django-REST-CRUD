from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Person
from .serializer import PersonSerializer


@api_view(['GET','POST','PUT','PATCH','DELETE'])
def person(request):
    if request.method == 'GET':
        objperson = Person.objects.all()
        print("object from orm qurey",objperson,"object from orm qurey")
        serializer = PersonSerializer(objperson,many = True)
        print("after the orm qurey what happes",serializer,"happenddddd")
        print("the final out put ",serializer.data,"this is serialiserddata")
        return Response(serializer.data)
    elif request.method == 'POST':
        print("post dataaaaaaaaaaaaaaaaaaaaaaaaa")
        data = request.data
        print(data,'data from the post method')
        serializer = PersonSerializer(data = data)
        print(serializer,'serializers from the post method')
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)
    elif request.method == 'PUT':
        data = request.data
        obj = Person.objects.get(id = data['id'])
        serializer = PersonSerializer(obj,data = data,partial = False)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)
    elif request.method == 'PATCH':
        data = request.data 
        obj = Person.objects.get(id = data['id'])
        serializer = PersonSerializer(obj,data = data, partial = True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)
    else:
        data = request.data
        obj = Person.objects.get(id = data['id'])
        obj.delete()
        return Response({'message': 'person deleted'})
        
    





@api_view(['GET','POST','PUT'])
def index(request):
    if request.method == 'GET':
        people_details = {
            'name' : 'vimal',
            'age' : 31,
            'job' : 'Developer'
        }
        return Response(people_details)
    elif request.method == 'POST':
        print("post mehod works")
        return Response("the method is Post method")
    elif request.method == 'PUT':
        return Response('the method is PUT method')
