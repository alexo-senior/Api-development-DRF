from django.urls import path
from . import views


urlpatterns = [
    path('students/',views.studentsView),
    
    #para manejar detalle por pk
    path('students/<int:pk>', views.studentDetailView),
    path('employees/', views.Employees.as_view()),#ruta para vista general empleado
    path('employees/<int:pk>/', views.EmployeeDetails.as_view()),#para usar con clave o id
    
]


