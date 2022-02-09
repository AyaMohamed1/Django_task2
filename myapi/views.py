import imp
from django.shortcuts import render
from html5lib import serialize
from student_register.models import intake, Student
from django.http import HttpResponse
from rest_framework import viewsets
from rest_framework.views import APIView
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import permissions
from .serializers import IntakeSerializer, StudentsSerializer
# Create your views here.
# def notser(request):
#     intakes = intake.objects.all()
#     request.session['intakes'] = intakes[0].id

#     # for intake in intakes:
#     #     pass
#     return HttpResponse('not ser error!')


@api_view(['POST'])
def deleteStudent (request,pk):
    student = Student.objects.get(pk=id)
    student.delete()
    return Response({'message': '{} student was deleted successfully!'.format(student.fullname)})

class IntakeList(viewsets.ModelViewSet):
    queryset = intake.objects.all()
    serializer_class = IntakeSerializer



class StudentList(viewsets.ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentsSerializer
    permission_classes = [permissions.IsAuthenticated]

