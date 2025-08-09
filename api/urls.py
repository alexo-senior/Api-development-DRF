from django.urls import path, include
from . import views
from rest_framework.routers import DefaultRouter

router = DefaultRouter()

#router se encargara de manejar todas las operaciones del crud
#registrar para la ruta de la app que manejara, sin barras

router.register('employee', views.EmployeeViewSet, basename='employee')


urlpatterns = [
    path('students/',views.studentsView),
    #para manejar detalle por pk
    path('students/<int:pk>', views.studentDetailView),
    
    #path('employees/', views.Employees.as_view()),#ruta para vista general empleado
    #path('employees/<int:pk>/', views.EmployeeDetails.as_view()),#para usar con clave o id
    
    #inclusionde las rutas del Router
    path('', include(router.urls)),
    
    path('blogs/', views.BlogsView.as_view()),
    path('comments/', views.CommentsView.as_view())
]






