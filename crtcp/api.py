from tastypie.contrib.gis.resources import ModelResource

from crtcp.models import UPAI

class UPAIResource(ModelResource):

	class Meta:
		queryset = UPAI.objects.all().geojson()

	def dehydrate(self, bundle):
		feature = {'type': 'Feature'}
		feature['properties'] = bundle.data
		feature['geometry'] = feature['properties']['the_geom']
		feature['resource_uri'] = feature['properties']['resource_uri']
		feature['id'] = feature['properties']['id']
		del(feature['properties']['id'])
		del(feature['properties']['resource_uri'])
		del(feature['properties']['the_geom'])
		return feature

	def alter_list_data_to_serialize(self, request, data_dict):
		if isinstance(data_dict, dict):
			if 'meta' in data_dict:
				# Get rid of the "meta".
				del(data_dict['meta'])
			data_dict['features'] = data_dict['objects']
			data_dict['type'] = 'FeatureCollection'
			del(data_dict['objects'])
		return data_dict
