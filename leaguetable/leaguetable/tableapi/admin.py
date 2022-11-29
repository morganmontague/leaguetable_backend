from django.contrib import admin
from .models import *

admin.site.register(CustomUser)
admin.site.register(Team)
admin.site.register(Player)
# Register your models here.
