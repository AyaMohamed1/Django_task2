import imp
from django.shortcuts import render
from html5lib import serialize
from student_register.models import intake, Student
from django.http import HttpResponse
from rest_framework import viewsets
from rest_framework import permissions
from .serializers import IntakeSerializer, StudentsSerializer
# Create your views here.
# def notser(request):
#     intakes = intake.objects.all()
#     request.session['intakes'] = intakes[0].id

#     # for intake in intakes:
#     #     pass
#     return HttpResponse('not ser error!')

class IntakeList(viewsets.ModelViewSet):
    queryset = intake.objects.all()
    serializer_class = IntakeSerializer

class StudentList(viewsets.ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentsSerializer
    permission_classes = [permissions.IsAuthenticated]

