from django.contrib import admin
from django.contrib.admin.sites import AdminSite
from django.contrib.auth.views import AuthenticationForm
from django.utils.translation import ugettext_lazy

from .models import User,UserProfile,CourseChoices,InstituteChoices,SemesterChoices,DisciplineChoices
# Register your models here.

"""TO be able to view Models in Django admin Panel we need to register"""

admin.site.register(UserProfile)
admin.site.register(CourseChoices)
admin.site.register(InstituteChoices)
admin.site.register(SemesterChoices)
admin.site.register(DisciplineChoices)


class UserAdmin(AdminSite):

    login_form = AuthenticationForm
    site_title = ugettext_lazy('MY Admin')
    site_header = ugettext_lazy("My Header")
    index_title = ugettext_lazy("MyIndex")

    def has_permission(self,request):

        return request.user.is_active

user_admin_site = UserAdmin(name = 'user admin')

user_admin_site.register(User)
