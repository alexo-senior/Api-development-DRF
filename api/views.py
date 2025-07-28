from django.shortcuts import render
from django.http import JsonResponse
from students.models import Students
from .serializers import StudentSerializer
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.views import APIView
#importar el modelo para la vista basada en clases
from employees.models import Employee
from .serializers import EmployeeSerializer
from django.http import Http404
#PARA LOS MIXIN
from rest_framework import mixins, generics


#VISTAS BASADAS EN FUNCIONES

@api_view(['GET', 'POST'])
def studentsView(request):
    if request.method == 'GET':
        students = Students.objects.all()
        serializer = StudentSerializer(students, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    elif request.method == 'POST':
        serializer = StudentSerializer(data=request.data)
        
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# con parametro de id
#tambien es get
@api_view(['GET', 'PUT', 'DELETE'])
def studentDetailView(request, pk):
    try:
        student = Students.objects.get(pk=pk)
        
    except Students.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    
    if request.method == 'GET':
        serializer = StudentSerializer(student)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    elif request.method == 'PUT':
        serializer = StudentSerializer(student, data=request.data)#se pasa student para actualizar ese dato
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
    elif request.method == 'DELETE':
        student.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
        
#vistas basadas en clases        
class Employees(APIView):
    def get(self, request):
        #Aquí puedes retornar una respuesta de ejemplo o implementar la lógica real
        employees = Employee.objects.all()
        serializer = EmployeeSerializer(employees, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    #crear dentro de la clase la funcion 
    def post(self, request):
        serializer = EmployeeSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
"""    
class EmployeeDetails(APIView):
        #primero se debe traer el dato del empleado de la bd con get_object
        #luego le pasamos el pk
    def get_object(self, pk):
        try:
            #employee = Employee.objects.get(pk=pk)
            return Employee.objects.get(pk=pk)
        except Employee.DoesNotExist:
            raise Http404
        #se solicita por la clave o el id 
    def get(self, request, pk):
        employee = self.get_object(pk)
        serializer = EmployeeSerializer(employee)#de EmployeeSerializer me trae employee
        return Response(serializer.data, status=status.HTTP_200_OK)#luego lo serializa con los datos
    
    
    def put(self, request, pk):
        Employee = self.get_object(pk)#obtener el objeto por pk
        serializer = EmployeeSerializer(Employee, data=request.data)#serializar de entrada
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    
    def delete(self, request, pk):
        #primero obtiene el objeto por medio del id
        employee = self.get_object(pk)
        #lo borra con delete
        employee.delete()
        #envia el mensaje de status en caso de consultar el eliminado
        return Response(status=status.HTTP_204_NO_CONTENT)
    """
    
    
class Employees(mixins.ListModelMixin, mixins.CreateModelMixin, generics.GenericAPIView):
    queryset = Employee.objects.all()#conjunro de consultas
    serializer_class = EmployeeSerializer
    
    #obtner la lista de todos los empleados
    def get(self, request):
        return self.list(request)
    #crear un nuevo empleado
    def post(self, request):
        return self.create(request)
    
    #recupera la informacion con la clave primaria o id y por put la actualiza
class EmployeeDetails(mixins.RetrieveModelMixin,mixins.UpdateModelMixin,mixins.DestroyModelMixin, generics.GenericAPIView):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer
    def get(self, request, pk):
        return self.retrieve(request, pk)#recupera o muestra un solo item
    
    #actualiza la informacion por medio del id
    def put(self, request, pk):
        return self.update(request, pk)
    
        
    def delete(self, request, pk):
        return self.destroy(request, pk)
    
    