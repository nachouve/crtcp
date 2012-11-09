import os
from django.contrib.gis.utils import LayerMapping
from crtcp.models import UPAI

upai_mapping = {
    'orden' : 'ORDEN',
    'tipo' : 'TIPO',
    'codigo' : 'CODIGO',
    'nome' : 'NOME',
    'id1' : 'ID1',
    'area' : 'Area',
    'area_pais' : 'Area_pais',
    'unidade_pa' : 'unidade_pa',
    'hectares' : 'Hectares',
    'etiqueta' : 'ETIQUETA',
    'geom' : 'POLYGON',
}

upai_shp = os.path.abspath(os.path.join(os.path.dirname(__file__), '/home/jlopez/UPAI/UNIDADES_PAISAXISTICAS.shp'))

lm = LayerMapping(UPAI, upai_shp, upai_mapping,
                      transform=False, encoding='iso-8859-1')

lm.save(strict=True, verbose=True)

