from django.shortcuts import render,get_object_or_404
from User_Registration.models import UserProfile
from django.contrib.auth.models import User

# Create your views here.

"""View for opening user DashBoard"""

def open_dashboard_view(request):
    user_id = request.user.id
    userprofile = get_object_or_404(UserProfile,user_id=user_id)
    user = get_object_or_404(User,id=user_id)

    context = {
        'user' : user,
        'userprofile' : userprofile
    }
    return render(request,'User/sidebar.html',context)
