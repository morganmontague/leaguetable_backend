from django.contrib import admin
from .models import *


class CustomUserAdmin(admin.ModelAdmin):
    model = CustomUser
# Register your models here.
admin.site.register(CustomUser, CustomUserAdmin)

# admin.site.register(CustomUser)
admin.site.register(Team)
admin.site.register(Player)
admin.site.register(Position)
admin.site.register(Nationality)
admin.site.register(Team_Players)
admin.site.register(Venue)
# Register your models here.
