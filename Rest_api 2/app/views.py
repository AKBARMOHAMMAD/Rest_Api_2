from django.contrib.messages.views import SuccessMessageMixin
from django.shortcuts import render
from django.views.generic import CreateView
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from app.EmployeeSerialization import MyEmployeeSerializer
from app.models import Employee


class MyEmployee(APIView):
    def get(self,request):
        qs= Employee.objects.all()
        ms= MyEmployeeSerializer(qs,many=True)
        return Response(ms.data)
    def post(self,request):
        emp=MyEmployeeSerializer(data=request.data)
        if emp.is_valid():
            emp.save()
            return Response(emp.data,status=status.HTTP_201_CREATED)
        return Response(emp.data,status=status.HTTP_400_BAD_REQUEST)

class EmployeeCreate(SuccessMessageMixin,CreateView):
    model = Employee
    template_name = "index.html"
    fields = ('name','age','contact_number','image')
    success_url = '/index/'
    success_message = 'Saved data'

