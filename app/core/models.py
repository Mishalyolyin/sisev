from django.db import models

class User(models.Model):
    name = models.CharField(max_length=100)

class Course(models.Model):
    title = models.CharField(max_length=200)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name="courses_created")
    participants = models.ManyToManyField(User, related_name="courses_joined")
