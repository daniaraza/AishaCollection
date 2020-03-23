from django.contrib import admin
from .models import Bride, UserInfo, User
from django.apps import AppConfig

admin.site.register(Bride)
admin.site.register(UserInfo)
