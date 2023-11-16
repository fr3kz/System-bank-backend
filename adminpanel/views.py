from django.shortcuts import render
from rest_framework import permissions
from rest_framework.views import APIView,Response

from accounts.models import Account
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



class DeleteEmployee(APIView):
    def get(self,request,usrid):
        user = User.objects.get(id=usrid)
        user.delete()
        return Response("User deleted")

class DeleteUser(APIView):
    def get(self,request,usrid):
        accounts = Account.objects.filter(account_owner=usrid)

        for account in accounts:
            account.delete()

        user = User.objects.get(id=usrid)
        user.delete()

        return Response("User deleted")

class User_count(APIView):
    permission_classes = (permissions.AllowAny,)
    def get(self,request):
        users_count = User.objects.all().count()
        print(users_count)
        contex = {'value':users_count}
        return Response(contex)



class Employe_count(APIView):
    permission_classes = (permissions.AllowAny,)
    def get(self,request):
        users_count = User.objects.filter(is_Employee=True).count()
        print(users_count)
        contex = {'value':users_count}
        return Response(contex)

class Ticket_count(APIView):
    permission_classes = (permissions.AllowAny,)
    def get(self,request):

        contex = {'value':'0'}
        return Response(contex)

class Ticket_list(APIView):
    permission_classes = (permissions.AllowAny,)
    #lista wszystkich wynikow
    def get(self,request):
        users = User.objects.filter(is_Activated=False)
        user_serializer = EmployeeSerializer(users,many=True)
        return Response(user_serializer.data, status=200)


class User_detail(APIView):
    #bedzie mialo funkcje post do usuwania i get do wyswietlania danych
    permission_classes = (permissions.AllowAny,)
    def get(self,request,userid):
        user = User.objects.get(id=userid)
        user_serializer = EmployeeSerializer(user)
        return Response(user_serializer.data, status=200)

    def post(self,request,userid):
        user = User.objects.get(id=userid)
        user.is_Activated = True
        user.save()

        contex = {'value':'User activated'}
        return Response(contex, status=200)



