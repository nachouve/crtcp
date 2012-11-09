from django.contrib.gis.db import models

class UPAI(models.Model):
    orden = models.IntegerField()
    tipo = models.CharField(max_length=50)
    codigo = models.IntegerField()
    nome = models.CharField(max_length=50)
    id1 = models.IntegerField()
    area = models.FloatField()
    area_pais = models.CharField(max_length=50)
    unidade_pa = models.CharField(max_length=50)
    hectares = models.FloatField()
    etiqueta = models.CharField(max_length=200)
    the_geom = models.MultiPolygonField(srid=23029)
    objects = models.GeoManager()
