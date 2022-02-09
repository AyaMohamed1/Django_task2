from django.urls import path,include
# from .views import notser
from rest_framework import routers
from .views import IntakeList, StudentList, deleteStudent
from student_register.models import intake, Student

router = routers.DefaultRouter()
router.register(r'Student', StudentList)
router.register(r'intake', IntakeList)
urlpatterns = [
    # path('', notser, name='notser'),
    path('', include(router.urls)),
    path('delete/<id>', deleteStudent),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]