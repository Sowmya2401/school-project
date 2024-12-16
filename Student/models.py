from django.db import models

agelist = [
    ("age1","2 to 5"),
    ("age2","5 to 8"),
    ("age3","8 to 10"),
    ("age4","10 to 12"),
]
time = [
    ("batch1","9 to 12"),
    ("batch2","12 to 2"),
    ("batch3","2 to 4"),
]

class Facilities(models.Model):
    title=models.CharField(max_length=50)
    description=models.TextField(max_length=200)

    def __str__(self):
        return self.title
class Teacher(models.Model):
    image=models.TextField(max_length=100)
    title=models.CharField(max_length=100)
    teacher_name=models.CharField(max_length=100)
    fees=models.IntegerField()
    age=models.CharField(choices=agelist,max_length=20)
    time=models.CharField(choices=time,max_length=20)
    capacity=models.IntegerField()

    def __str__(self):
        return self.title
class Appointment(models.Model):
    name=models.CharField(max_length=50)
    email=models.CharField(max_length=50)
    child_name=models.CharField(max_length=50)
    child_age=models.CharField(max_length=50)
    message=models.TextField(max_length=500)

    def __str__(self):
        return self.name



    

