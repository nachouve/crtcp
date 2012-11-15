from django.contrib.gis.db import models

class upai(models.Model):
    tipo = models.IntegerField()
    area_paisaxe = models.CharField(max_length=100)
    unidad_paisaxe = models.CharField(max_length=100)
    hectareas = models.FloatField()

    geom = models.MultiPolygonField(srid=23029)
    objects = models.GeoManager()

    def __unicode__(self):
        return str(self.tipo)+'-'+self.unidad_paisaxe

    class Meta:
        ordering = ["area_paisaxe", "unidad_paisaxe"]