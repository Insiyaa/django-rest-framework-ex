from django.shortcuts import render

from rest_framework import status 

from toys.models import Toy 
from toys.serializers import ToySerializer 

# The @api_view decorator allows us to specify which are the HTTP verbs that the function to which
# it is applied can process
from rest_framework.decorators import api_view

# The Response class renders the provided data into the appropriate content type and returns it to
# the client that made the request.
from rest_framework.response import Response
 

 
@api_view(['GET', 'POST'])
def toy_list(request):
    # Return toys 
    if request.method == 'GET': 
        toys = Toy.objects.all() 
        toys_serializer = ToySerializer(toys, many=True) 
        return Response(toys_serializer.data) 

    # Create a toy
    elif request.method == 'POST': 
        toy_serializer = ToySerializer(data=request.data) 
        if toy_serializer.is_valid(): 
            toy_serializer.save() 
            return Response(toy_serializer.data, status=status.HTTP_201_CREATED) 
        return Response(toy_serializer.errors, status=status.HTTP_400_BAD_REQUEST) 
 
#  Working with single toy
@api_view(['GET', 'PUT', 'DELETE'])
def toy_detail(request, pk): 
    try: 
        toy = Toy.objects.get(pk=pk) 
    except Toy.DoesNotExist: 
        return Response(status=status.HTTP_404_NOT_FOUND) 

    # Return a single toy's data
    if request.method == 'GET': 
        toy_serializer = ToySerializer(toy) 
        return Response(toy_serializer.data) 
 
    # Update toy's data
    elif request.method == 'PUT': 
        toy_serializer = ToySerializer(toy, data=request.data) 
        if toy_serializer.is_valid(): 
            toy_serializer.save() 
            return JSONResponse(toy_serializer.data) 
        return Response(toy_serializer.errors, status=status.HTTP_400_BAD_REQUEST) 
 
    # Delete toy
    elif request.method == 'DELETE': 
        toy.delete() 
        return Response(status=status.HTTP_204_NO_CONTENT)
