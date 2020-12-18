from django.db import models
from django.urls import reverse


# SuperUserInformation
# User: Ankur
# Email: training@home.com
# Password: testpassword

class School(models.Model):
    name = models.CharField(max_length=256)
    principal = models.CharField(max_length=256)
    location = models.CharField(max_length=256)

    def __str__(self):
        return self.name

    # CreateView -
    # 1) Django CreateView is automatically creating a default html template that is expecting.
    # It is expecting into be in format of all lower case model name (School and then _form)
    # i.e., school_form.html. Always suggest to use default name for template and create school_form.html
    # to add form to create new School.
    # 2) Also, define a get_absolute_url method on the Model (here School). This is linked with CreateView
    # to tell create view where to go after creating a page. Here, go back and reverse and figure out
    # you should go to the detail page for whatever the primary key of school you have just created.
    def get_absolute_url(self):
        return reverse("crudapp:detail", kwargs={'pk': self.pk})


class Student(models.Model):
    name = models.CharField(max_length=256)
    age = models.PositiveIntegerField()
    school = models.ForeignKey(School, related_name='students', on_delete=models.CASCADE)

    def __str__(self):
        return self.name
