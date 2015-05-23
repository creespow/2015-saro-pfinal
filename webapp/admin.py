from django.contrib import admin

from models import event, user_choices, choice

# Register your models here.

admin.site.register(event)
admin.site.register(user_choices)
admin.site.register(choice)