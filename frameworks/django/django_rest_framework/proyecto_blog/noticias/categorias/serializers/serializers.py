from rest_framework import serializers
from categorias.models import Categoria


class CategoriaSerializer(serializers.ModelSerializer):

	class Meta:
		model = Categoria
		fields = ['id', 'title', 'slug', 'publicado']