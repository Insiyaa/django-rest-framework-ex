from django.shortcuts import render

# Represents an HTTP response with string content.
from django.http import HttpResponse

# To ensure that the view sets a CSRF (short for Cross-Site Request Forgery) cookie
from django.views.decorators.csrf import csrf_exempt 
from rest_framework.renderers import JSONRenderer 
from rest_framework.parsers import JSONParser 
from rest_framework import status 
from toys.models import Toy 
from toys.serializers import ToySerializer 
 
 
#  django.http.JsonResponse class has accomplished the same goal
class JSONResponse(HttpResponse): 
    def __init__(self, data, **kwargs): 
        content = JSONRenderer().render(data) 
        kwargs['content_type'] = 'application/json' 
        super(JSONResponse, self).__init__(content, **kwargs) 
 
 
@csrf_exempt 
def toy_list(request):
    # Return toys 
    if request.method == 'GET': 
        toys = Toy.objects.all() 
        toys_serializer = ToySerializer(toys, many=True) 
        return JSONResponse(toys_serializer.data) 

    # Create a toy
    elif request.method == 'POST': 
        toy_data = JSONParser().parse(request) 
        toy_serializer = ToySerializer(data=toy_data) 
        if toy_serializer.is_valid(): 
            toy_serializer.save() 
            return JSONResponse(toy_serializer.data, \
                status=status.HTTP_201_CREATED) 
        return JSONResponse(toy_serializer.errors, \
            status=status.HTTP_400_BAD_REQUEST) 
 
#  Working with single toy
@csrf_exempt 
def toy_detail(request, pk): 
    try: 
        toy = Toy.objects.get(pk=pk) 
    except Toy.DoesNotExist: 
        return HttpResponse(status=status.HTTP_404_NOT_FOUND) 

    # Return a single toy's data
    if request.method == 'GET': 
        toy_serializer = ToySerializer(toy) 
        return JSONResponse(toy_serializer.data) 
 
    # Update toy's data
    elif request.method == 'PUT': 
        toy_data = JSONParser().parse(request) 
        toy_serializer = ToySerializer(toy, data=toy_data) 
        if toy_serializer.is_valid(): 
            toy_serializer.save() 
            return JSONResponse(toy_serializer.data) 
        return JSONResponse(toy_serializer.errors, \
            status=status.HTTP_400_BAD_REQUEST) 
 
    # Delete toy
    elif request.method == 'DELETE': 
        toy.delete() 
        return HttpResponse(status=status.HTTP_204_NO_CONTENT)
