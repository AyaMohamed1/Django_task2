from rest_framework import serializers
from student_register.models import intake, Student

class IntakeSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = intake
        fields = ['id', 'name']


class StudentsSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Student
        fields = ['fullname', 'st_code', 'phone']