from django import forms

from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import UserProfile,CourseChoices,InstituteChoices,SemesterChoices,DisciplineChoices

"""To Create a user we used Django UserCreationForm"""
class CreateUserForm(UserCreationForm):
    first_name  = forms.CharField(required = True)
    last_name = forms.CharField(required = True)
    email = forms.CharField(required = True, widget = forms.EmailInput(attrs={'class': 'validate',}))
    class Meta:
        model = User
        fields = ['first_name','last_name','username','email','password1','password2']
        # widgets = {
        #     'email' : forms.CharField(required=True, widget=forms.EmailInput(attrs={'class': 'validate'}))
        # }

"""To save a user's profile details we used ModelForm"""
class UserRegistrationForm(forms.ModelForm):
    InstituteList = []
    CourseList = []
    SemesterList = []
    DisciplineList = []
    Institute = forms.ModelChoiceField(queryset = InstituteChoices.objects.all(), empty_label = 'Select Institute', required = False)
    Course = forms.ModelChoiceField(queryset = CourseChoices.objects.all(), empty_label = 'Select Course', required = False)
    Discipline = forms.ModelChoiceField(queryset = DisciplineChoices.objects.all(), empty_label = 'Select Discipline', required = False)
    isFaculty = forms.ChoiceField(choices = [(True,'Faculty'),(False,'Student')], widget = forms.RadioSelect(attrs = { 'id' : "radio", 'onchange' : "change()" }))
    Semester = forms.ModelChoiceField(queryset = SemesterChoices.objects.all(), empty_label = 'Select Semester', required = False)
    DOB = forms.DateField(widget=forms.SelectDateWidget(years = range(1950,2020)))

    class Meta :
        model = UserProfile
        fields = [
            'isFaculty',
            'Id',
            'DOB',
            'MobileNumber',
            'Institute',
            'Course',
            'Discipline',
            'Semester'
        ]

""" For updating user details used UserChangeForm"""

class EditProfileForm(UserChangeForm):
    class Meta:
        model = User
        fields = [
            'first_name',
            'last_name',
            'username',
        ]
