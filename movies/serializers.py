from rest_framework import serializers
from movies.models import Movie
from genres.models import Genre
from actors.models import Actor


class MovieModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movie
        fields = '__all__'

    def validate_release_date(self, value):
        if value.year < 1990:
            raise serializers.ValidationError('A data de lançaento não pode ser anterior a 1991.')
        return value
    
    def validate_resume(self,value):
        if len(value) > 200:
            raise serializers.ValidationError('Resumo não deve ser maior do que 200 caracteres.')
        return value