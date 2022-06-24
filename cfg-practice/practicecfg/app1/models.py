from django.db import models

# Create your models here.

option = (
    ("Maths", "Maths"),
    ("Physics", "Physics"),
    ("Chemistry", "Chemistry"),
    ("Biology", "Biology"),
)


class Student(models.Model):
    name = models.CharField(max_length=30)
    email = models.CharField(max_length=20)
    phone_no = models.IntegerField()
    subject = models.CharField(max_length=30, choices=option)
    homework = models.FileField(blank=True)
    result = models.CharField(max_length=30, default="not checked")
    remarks = models.TextField(blank=True)

    def __str__(self):
        return self.name
