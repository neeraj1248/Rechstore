from django.contrib import admin

# Register your models here.

from .models import Accounts
admin.site.register(Accounts)

from .models import Token
admin.site.register(Token)
