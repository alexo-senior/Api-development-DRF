from django.db import models


class Employee(models.Model):
    employee_id = models.CharField(max_length=20)
    employee_name = models.CharField(max_length=50)
    designation = models.CharField(max_length=50)
    
    
    def  __string__(self):
        return self.employee_name
    

    
