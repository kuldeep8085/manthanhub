from django.contrib.admin import AdminSite
from django.contrib import admin
from django.contrib.auth.models import User, Group

# Register your models here.

from .models import Question
from .models import Choice
from .models import Reaction


# admin.site.unregister(User)
# admin.site.unregister(Group)

class PollsAdminSite(AdminSite):
	site_header = "UMSRA Admin"
	site_title = "UMSRA Admin Portal"
	index_title = "Welcome to UMSRA Researcher Portal"


admin.site.register(Question)

admin.site.register(Choice)
admin.site.register(Reaction)


polls_admin_site = PollsAdminSite(name='polls_admin')


polls_admin_site.register(Question)
polls_admin_site.register(Reaction)
polls_admin_site.register(Choice)
