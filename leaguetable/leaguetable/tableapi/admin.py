from django.contrib import admin
from .models import *

admin.site.register(CustomUser)
admin.site.register(Team)
admin.site.register(Player)
admin.site.register(Position)
admin.site.register(Nationality)
admin.site.register(Team_Players)
# Register your models here.
