from django.contrib import admin

from .models import User, PhoneCode, Adresses

admin.site.register(User)
admin.site.register(PhoneCode)
admin.site.register(Adresses)
