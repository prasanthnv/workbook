from rest_framework.views import APIView
from rest_framework.response import Response
from employee.models import Employee
from employee.serializers import EmployeeSerializer, EmployeeListSerializer
from rest_framework import status


class EmployeeController(APIView):
    def get(self, request):
        employees = Employee.objects.all()
        serializer = EmployeeListSerializer(employees, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = EmployeeSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
