from django.shortcuts import render
from .models import student
from .serializers import studentserializer

from rest_framework import viewsets
from rest_framework.authentication import BasicAuthentication ,SessionAuthentication
from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly



class studentmodelviewset(viewsets.ModelViewSet):
    queryset = student.objects.all()    
    serializer_class = studentserializer
    authentication_classes = [SessionAuthentication]
    # permission_classes = [IsAuthenticated]
    permission_classes = [IsAuthenticatedOrReadOnly]
                                

                                                    
