from django.contrib import admin

from .models import User, PhoneCode

admin.site.register(User)
admin.site.register(PhoneCode)
