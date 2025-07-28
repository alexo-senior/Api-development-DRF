from django.db import models

#create model student
class Students(models.Model):
    student_id = models.CharField(max_length=10)
    name = models.CharField(max_length=50)
    branch = models.CharField(max_length=50)
    
    
    def __str__(self):
        return self.name
    
    
