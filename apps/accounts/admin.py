from django.contrib import admin
from apps.accounts.models import User
from auth_pack.admin import EmailUserAdmin
from django.contrib.auth.models import Group

admin.site.register(User, EmailUserAdmin)
admin.site.unregister(Group)
