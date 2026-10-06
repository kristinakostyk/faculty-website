from django.db import models


class Department(models.Model):
    name = models.CharField(max_length=200)
    head = models.ForeignKey(
    'Teacher',
        on_delete=models.SET_NULL,
        null=True,
        related_name='teachers'
    )
    def __str__(self):
        return self.name

class Teacher(models.Model):
    name = models.CharField(max_length=200)
    position = models.CharField(max_length=200)
    degree = models.CharField(max_length=200)
    department = models.ForeignKey(
        Department,
        on_delete=models.CASCADE,
        related_name='teachers'
    )

    def __str__(self):
        return self.name

class Program(models.Model):
    name = models.CharField(max_length=200)
    code = models.CharField(max_length=50)
    description = models.TextField()
    coordinator_name = models.CharField(max_length=200)
    coordinator_contact = models.CharField(max_length=200)
    department = models.ForeignKey(
        Department,
        on_delete=models.CASCADE,
        related_name='programs'
    )
    disciplines = models.TextField()

    def __str__(self):
        return self.name



class HomePage(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    contact_info = models.TextField()

    def __str__(self):
        return self.title
