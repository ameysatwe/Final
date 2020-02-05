from django.shortcuts import render,redirect,get_object_or_404
from django.core.mail import send_mail
from django.contrib.auth.forms import AuthenticationForm, PasswordChangeForm
from django.contrib.auth import login,logout, update_session_auth_hash
from User_Registration.models import UserProfile
from django.contrib.auth.models import User
from django.utils.crypto import get_random_string
from django.core.mail import send_mail
from outreachdemo.settings import EMAIL_HOST_USER
from .models import UserProfile
from django.contrib.auth.models import User
from django.http import Http404
from django.contrib import messages

from datetime import timedelta

from .forms import UserRegistrationForm, EditProfileForm
from .forms import CreateUserForm

# Create your views here.
""" View for registering new user """

def user_registration_view(request):
    form1 = CreateUserForm(request.POST or None)
    form = UserRegistrationForm(request.POST or None)
    if(form.is_valid() and form1.is_valid()):
        UID = get_random_string(length = 32)
        user = form1.save()
        profile = form.save(commit = False)
        profile.user = user
        profile.UID = UID
        profile.save()
        message = "outreachdemointern.herokuapp.com/verification/"+str(form1.cleaned_data['username'])+"/"+UID
        send_mail("Verification", message, EMAIL_HOST_USER, [form1.cleaned_data['email']],fail_silently = False)
        return redirect('User:login')
        form1 = CreateUserForm()
        form = UserRegistrationForm()
        messages.success(request,"Registration Successful")
    else:
        messages.error(request,"Please check for errors")
    return render(request, 'User/signup.html',{
    'form' : form,
    'form1' : form1,
    })

""" View for login"""

def login_view(request):
    if(request.method == 'POST'):
        form = AuthenticationForm(data = request.POST)
        if form.is_valid() and form.get_user().user_profile.Verified:
            user = form.get_user()
            login(request,user)
            return redirect('DashBoard:dashboard')
        if form.is_valid() and form.get_user().user_profile.Verified == False:
            raise Http404("Please verify Account")
    else:
        form = AuthenticationForm()
    return render(request,'User/login.html',{'form' : form})


"""View for Updating user details"""

def update_view(request):
    user = get_object_or_404(User,id = request.user.id)
    userProfile = get_object_or_404(UserProfile,user_id = request.user.id)
    form1 = EditProfileForm(request.POST or None,instance = user)
    form = UserRegistrationForm(request.POST or None, instance = userProfile)
    if(form.is_valid() and form1.is_valid()):
        user = form1.save()
        profile = form.save(commit = False)
        profile.user = user
        if(profile.isFaculty):
            profile.Institute = "NA"
            profile.Semester = "NA"
            profile.Course = "NA"
            profile.Discipline = "NA"
        profile.save()
        return redirect('DashBoard:dashboard')
    return render(request, 'User/usereditprofile.html',{
    'form' : form,
    'form1' : form1,
    })

"""View for Logout"""

def logout_view(request):
    logout(request)
    return redirect('/')

"""View for Verification"""

def verification_view(request,username,uid):
    user = User.objects.get(username = username)
    if(user):
        if(user.user_profile.UID == uid):
            user.user_profile.Verified = True
            user.user_profile.save()
            return redirect('User:login')
    raise Http404("Not Verified")

"""View for Change Password"""

def change_password(request):
    if request.method == 'POST':
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            user = form.save()

            """Rehashing of password is done using update_session_auth_hash"""

            update_session_auth_hash(request, user)
            messages.success(request, 'Your password was successfully updated!')
            return redirect('DashBoard:dashboard')
        else:
            messages.error(request, 'Please Check your passwords.')
    else:
        form = PasswordChangeForm(request.user)
    return render(request, 'User/change_password.html', {
        'form': form
    })


def showIndex(request):
    return render(request, 'User/index (2).html')