#from django.shortcuts import render

# Create your views here.
from django.contrib.auth.models import *
from django.contrib.auth import *
from rest_framework import viewsets
from rest_framework.views import APIView
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework import status
#from django.shortcuts import render_to_response
from django.template import RequestContext
from django_filters.rest_framework import DjangoFilterBackend


from django.shortcuts import *

# Import models
from django.db import models
from django.contrib.auth.models import *
from api.models import *

#REST API
from rest_framework import viewsets, filters, parsers, renderers
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from api.serializers import PlantSerializer, SpeciesSerializer

from django.contrib.auth import authenticate, login, logout
from rest_framework.permissions import *
from rest_framework.decorators import *
from rest_framework.authentication import *

#filters
#from filters.mixins import *

from api.pagination import *
import json, datetime, pytz
from django.core import serializers
import requests

def home(request):
   """
   Send requests to / to the ember.js clientside app
   """
   return render_to_response('index.html',
               {}, RequestContext(request))
#artifact code from code base
"""
def xss_example(request):
 
  Send requests to xss-example/ to the insecure client app
  
  return render_to_response('dumb-test-app/index.html',
              {}, RequestContext(request))
"""
class Session(APIView):
    permission_classes = (AllowAny,)
    def form_response(self, isauthenticated, userid, username, error=""):
        data = {
            'isauthenticated': isauthenticated,
            'userid': userid,
            'username': username
        }
        if error:
            data['message'] = error

        return Response(data)

    def get(self, request, *args, **kwargs):
        # Get the current user
        if request.user.is_authenticated():
            return self.form_response(True, request.user.id, request.user.username)
        return self.form_response(False, None, None)

    def post(self, request, *args, **kwargs):
        # Login
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                login(request, user)
                return self.form_response(True, user.id, user.username)
            return self.form_response(False, None, None, "Account is suspended")
        return self.form_response(False, None, None, "Invalid username or password")

    def delete(self, request, *args, **kwargs):
        # Logout
        logout(request)
        return Response(status=status.HTTP_204_NO_CONTENT)
"""
class Events(APIView):
    permission_classes = (AllowAny,)
    parser_classes = (parsers.JSONParser,parsers.FormParser)
    renderer_classes = (renderers.JSONRenderer, )
"""
#handles the HTTP requests of plants when a pk is provided and allows GET and PUT requests
class PlantDetail(APIView):
   permission_classes = (AllowAny,)
   def get(self, request, pk, format=None):
        #handles the read operation for a single object
      #/api/plant/[pk]
      # the url file is going to route request to the method, serialize it and send it back
      try:
         plant = Plant.objects.get(pk=pk)
         serializer = PlantSerializer(plant)
         return Response(serializer.data)
      except Plant.DoesNotExist:
         raise Http404
      
   def put(self, request, pk, format=None):
      #/api/plant/[pk] http put request
      try:
         plant = Plant.objects.get(pk=pk)
         serializer = PlantSerializer(plant, data=request.data)
         if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
      except Plant.DoesNotExist:
         raise Http404
#handles the HTTP requests of plants when a pk is not provided and allows GET and POST requests, will list all entries in model
class PlantList(APIView):
   def get(self, request, format=None): #handles the read operation for a list of objects
      plant = Plant.objects.all()
      serializer = PlantSerializer(plant, many=True)
      return Response(serializer.data)
   
   def post(self, request, format=None):
      serializer = PlantSerializer(data=request.data)
      if serializer.is_valid():
         serializer.save()
         return Response(serializer.data, status=status.HTTP_201_CREATED)
      return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
   
#handles the HTTP requests of species when a pk is provided and allows GET requests, only allows GEt since all edits should be handled in admin console
class SpeciesDetail(APIView):
   permission_classes = (AllowAny,)
   def get(self, request, pk, format=None):
      try:
         species = Species.objects.get(pk=pk)
         serializer = SpeciesSerializer(species)
         return Response(serializer.data)
      except Species.DoesNotExist:
         raise Http404
"""
   def put(self, request, pk, format=None):
      try:
         species = Species.objects.get(pk=pk)
         serializer = SpeciesSerializer(species, data=request.data)
         if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
      except Species.DoesNotExist:
         raise Http404
      
   def delete(self, request, pk, format=None):
      try:
         species = Species.objects.get(pk=pk)   
         species.delete()
         return Response(status=status.HTTP_204_NO_CONTENT)
      except Species.DoesNotExist:
         raise Http404
"""
#handles the HTTP requests of species when a pk is not provided and allows GET requests, only allows GEt since all edits should be handled in admin console, lists all entries
class SpeciesList(APIView):
   def get(self, request, format=None): #handles the read operation for a list of objects
      species = Species.objects.all()
      serializer = SpeciesSerializer(species, many=True)
      return Response(serializer.data)
"""   
   def post(self, request, format=None):
      serializer = SpeciesSerializer(data=request.data)
      if serializer.is_valid():
         serializer.save()
         return Response(serializer.data, status=status.HTTP_201_CREATED)
      return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
"""
