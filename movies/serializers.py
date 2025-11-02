from rest_framework import serializers
from movies.models import Movie
from genres.models import Genre
from actors.models import Actor


class MovieSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movie
        fields = '__all__'