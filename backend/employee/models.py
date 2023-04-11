from django.db import models

# Create your models here.


class Department(models.Model):
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=100, blank=True, null=True)

    def __str__(self):
        return self.name


class Employee(models.Model):
    employee_id = models.CharField(max_length=10, unique=True, null=False)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField(max_length=50, null=False, unique=True)
    password = models.CharField(
        max_length=50, null=False, default='1Barcelona')
    department = models.ForeignKey(
        Department, on_delete=models.CASCADE, null=True)

    def __str__(self):
        # return as employee first name and last name [employee id] ~ department
        return f'{self.first_name} {self.last_name} [{self.employee_id}] ~ {self.department}'
