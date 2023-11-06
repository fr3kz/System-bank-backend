from django.shortcuts import render
from rest_framework.views import APIView,Response
from users.models import User
from .serializers import EmployeeSerializer
# Create your views here.
class ShowEmployess(APIView):
    def get(self,request):
        employees = User.objects.filter(is_Employee=True)
        emp_serializer = EmployeeSerializer(employees,many=True)
        return Response(emp_serializer.data)



class ShowEmployByID(APIView):
    def get(self,request,pk):
        employee = User.objects.get(id=pk)
        emp_serializer = EmployeeSerializer(employee)
        return Response(emp_serializer.data)

class CreateEmployee(APIView):
    def post(self,request):
        employe_serializer = EmployeeSerializer(data=request.data)

        if employe_serializer.is_valid(raise_exception=True):
            employe_serializer.save()
            return Response(employe_serializer.data)
        else:
            return Response(employe_serializer.errors)


class ActivateUser(APIView):
    def get(self,request,usrid):
        user = User.objects.get(id=usrid)
        user.is_Activated = True
        user.save()
        return Response("User activated")