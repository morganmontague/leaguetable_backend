from django.contrib import admin
from .models import *

admin.site.register(CustomUser)
admin.site.register(Team)
admin.site.register(Player)
admin.site.register(Position)
# Register your models here.
