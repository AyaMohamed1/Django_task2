from cProfile import label
from pyexpat import model
from turtle import st
from django import forms
from .models import Student


class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = ('fullname', 'st_code', 'phone', 'track')
        labels = {
            'fullname':'Student name',
            'st_code' : "id",
            'track': 'track_id'
        }
    # def __init__(self, *args, **kwargs):
    #     super(StudentForm, self).__init__(*args, **kwargs)
    #     self.fields['track'].empty_label = 'Select'