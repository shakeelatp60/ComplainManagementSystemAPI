from django.shortcuts import render
from rest_framework import viewsets
from .models import ComplainRecord
from .serializers import ComplainRecordSerializer
from rest_framework.authentication import SessionAuthentication
from rest_framework.permissions import DjangoModelPermissions

class ComplainRecordView(viewsets.ModelViewSet):
    queryset = ComplainRecord.objects.all()
    serializer_class = ComplainRecordSerializer
    authentication_classes = [SessionAuthentication]
    permission_classes = [DjangoModelPermissions]
