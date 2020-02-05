"""User_Registration URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.urls import include,path
from . import views
from User_Registration.admin import user_admin_site

app_name = 'User'
urlpatterns = [
    path('userregistration/',views.user_registration_view, name = 'User Registration'),
    path('login/',views.login_view, name = 'login'),
    path('update/',views.update_view, name = 'update'),
    path('logout/',views.logout_view, name = 'logout'),
    path('change_password/',views.change_password, name = 'change password'),
    path('verification/<username>/<uid>',views.verification_view, name = 'verification  '),
    path('user-admin/',user_admin_site.urls)

]
