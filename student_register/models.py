from django.db import models

# Create your models here.
class track(models.Model):
    name = models.CharField(max_length=30)

    def __str__(self):
        return self.name

class Student(models.Model):
    fullname = models.CharField(max_length=30)
    st_code = models.CharField(max_length=30)
    phone = models.CharField(max_length=30)
    track = models.ForeignKey(track, on_delete=models.CASCADE)
