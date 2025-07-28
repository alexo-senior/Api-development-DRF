from django.shortcuts import render
from django.http import HttpResponse

#
def students(request):
    #en caso que quiera imprimir algo en http
    students = [
        {'id': 1, 'name': 'Alexis', 'age': 51}
    ]
    #return HttpResponse('<h2>Hello Developers</h2>')
    return HttpResponse(students)





