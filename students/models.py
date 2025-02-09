from django.db import models

class Student(models.Model):
    student_number = models.PositiveIntegerField()
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField(max_length=100)
    field_of_study = models.CharField(max_length=50)
    gpa = models.FloatField()
    photo = models.ImageField(upload_to='student_photos/', blank=True, null=True)

    def __str__(self):
        return f'Student: {self.first_name} {self.last_name} {self.student_number}'
 