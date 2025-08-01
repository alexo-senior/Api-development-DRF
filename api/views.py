from django.shortcuts import render, get_object_or_404#trae los datos o muestra errror 404
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
from rest_framework import mixins, generics, viewsets


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
    
    #METODOS CON MIXINS, SIMPLIFICA CODIGO YA QUE ENCAPSULA LOS METODOS CRUD
    #sin embargo aun se tiene que escribir las funciones con los metodos normales
    #como los son get, post, el retrieve,put y el delete
""""""

#GENERICS
#la clase se debe colocar con un nombre diferente al importado desde employees.model
#la cual es Employee, es decir no puede tener el mismo nombre de la clase importada
#usando CreateAPIView se renderiza un formulario para post y aparece en la web

#Listar y crear
"""class Employees(generics.ListAPIView, generics.CreateAPIView):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer
    
    
#Retrieve(recuperar un objeto), actualizar y borrar    
class EmployeeDetails(generics.RetrieveAPIView, generics.UpdateAPIView, generics.DestroyAPIView):
    queryset =Employee.objects.all()
    serializer_class = EmployeeSerializer
    lookup_field = 'pk'  #con solo eso se habilita para buscar por pk
"""


#listar objetos con Viewset
class EmployeeViewset(viewsets.ViewSet):
    def list(self, request):
        queryset = Employee.objects.all()
        serializer = EmployeeSerializer(queryset, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    #Crear con Viewset
    def create(self, request):
        serializer = EmployeeSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def retrieve(self, request, pk=None):
        employee = get_object_or_404(Employee, pk=pk)
        serializer = EmployeeSerializer(employee)
        return Response(serializer.data, status=status.HTTP_200_OK)
        
    
    
    def update(self, request, pk=None):
        employee = get_object_or_404(Employee, pk=pk)
        serializer = EmployeeSerializer(employee, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)
    
    
    def delete(self, request, pk=None):
        employee = get_object_or_404(Employee, pk=pk)
        employee.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
                        
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    



    

    
    
    
    