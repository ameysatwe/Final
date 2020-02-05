from django.db import models
from django.contrib.auth.models import User


# Create your models here.


class UserProfile(models.Model):

    """ To Map a User To Profile used OneToOneField """

    user = models.OneToOneField(User, on_delete = models.CASCADE, related_name = 'user_profile')
    isFaculty = models.BooleanField(default = False)
    Id = models.CharField(max_length = 10, primary_key = True)
    DOB = models.DateField()
    MobileNumber = models.CharField(max_length = 13)
    Institute = models.CharField(max_length = 100, default = "NA")
    Course = models.CharField(max_length = 100, default = "NA")
    Discipline = models.CharField(max_length = 100, default = "NA")
    Semester = models.CharField(max_length = 100, default = "NA")
    Verified = models.BooleanField(default = False)
    UID = models.CharField(max_length = 32, default = None)

    def __str__(self):
        return self.user.username

"""Model for Institute Choices"""

class InstituteChoices(models.Model):
    Name = models.CharField(max_length = 100)
    Key = models.CharField(max_length = 100, primary_key = True)
    def __str__(self):
        return self.Name

"""Model for Semester Choices"""

class SemesterChoices(models.Model):
    Name = models.CharField(max_length = 100)
    Key = models.CharField(max_length = 100, primary_key = True)
    def __str__(self):
        return self.Name

"""Model for Courses Choices"""

class CourseChoices(models.Model):
    Name = models.CharField(max_length = 100)
    Key = models.CharField(max_length = 100, primary_key = True)
    def __str__(self):
        return self.Name

"""Model for Discipline Choices"""


class DisciplineChoices(models.Model):
    Name = models.CharField(max_length = 100)
    Key = models.CharField(max_length = 100, primary_key = True)
    def __str__(self):
        return self.Name
