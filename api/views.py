from django.shortcuts import render
from rest_framework import viewsets
from api.models import Company, Employee
from api.serializers import CompanySerializers, EmployeeSerializers
from rest_framework.decorators import action
from rest_framework.response import Response
# Create your views here.

class CompanyViewSet(viewsets.ModelViewSet):

    queryset = Company.objects.all()
    serializer_class = CompanySerializers

    @action(detail=True, methods=['get'])
    def employee(self, request, pk=None):
      try:
          company = Company.objects.get(pk=pk)
          emps = Employee.objects.filter(company=company)
          emps_serializers= EmployeeSerializers(emps,many=True,context={'request':request})
          return Response(emps_serializers.data)
      except Exception as e:
          print(e)
          return Response({
              'message': 'Company is not exits !! error '
          })
class EmployeeViewSet(viewsets.ModelViewSet):

    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializers