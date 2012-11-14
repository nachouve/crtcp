from django.contrib.gis import admin
from models import upai

admin.site.register(upai, admin.GeoModelAdmin)
