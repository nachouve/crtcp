import os
from django.contrib.gis.utils import LayerMapping
from models import upai

upai_mapping = {
    'tipo' : 'TIPO',
    'area_paisaxe' : 'Area_pais',
    'unidad_paisaxe' : 'unidade_pa',
    'hectareas' : 'Hectares',
    'geom' : 'MULTIPOLYGON',
}

upais_shp = os.path.abspath(os.path.join(os.path.dirname(__file__), '../shp/', 'UNIDADES_PAISAXISTICAS.shp'))

def run(verbose=True):
    lm = LayerMapping(upai, upais_shp, upai_mapping,
                      transform=False, encoding='iso-8859-1')

    lm.save(strict=True, verbose=verbose)
