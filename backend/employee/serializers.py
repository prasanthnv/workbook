from rest_framework import serializers
from .models import Employee, Department


class DepartmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Department
        fields = [
            'id',
            'name',
            'description'
        ]


class EmployeeListSerializer(serializers.ModelSerializer):
    # department = serializers.PrimaryKeyRelatedField(
    #     queryset=Department.objects.all())
    # department =
    department = DepartmentSerializer()

    class Meta:
        model = Employee
        # exclude = ['password']
        fields = [
            'employee_id',
            'first_name',
            'last_name',
            'email',
            'department'
        ]


class EmployeeSerializer(serializers.ModelSerializer):
    # department = serializers.PrimaryKeyRelatedField(
    #     queryset=Department.objects.all())
    # department =
    class Meta:
        model = Employee
        # exclude = ['password']
        fields = [
            'employee_id',
            'first_name',
            'last_name',
            'email',
            'password',
            'department'
        ]
        # make password field write only
        extra_kwargs = {
            'password': {'write_only': True}
        }

    def create(self, validated_data):
        return Employee.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.employee_id = validated_data.get(
            'employee_id', instance.employee_id)
        instance.first_name = validated_data.get(
            'first_name', instance.first_name)
        instance.last_name = validated_data.get(
            'last_name', instance.last_name)
        instance.email = validated_data.get('email', instance.email)
        instance.password = validated_data.get(
            'password', instance.password)
        instance.department = validated_data.get(
            'department', instance.department)
        instance.save()
        return instance
