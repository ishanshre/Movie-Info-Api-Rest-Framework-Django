from rest_framework import serializers
from apps_watchlist.models import Movie



class MovieSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movie
        fields = ['id','title','descriptions','active']

    # def create(self, validated_data):
    #     return Movie.objects.create(validated_data)
    
    # def update(self, instance, validated_data):
    #     instance.title = validated_data.get('title', instance.title)
    #     instance.descriptions = validated_data.get('descriptions', instance.descriptions)
    #     instance.active = validated_data.get('active', instance.active)
    #     instance.save()
    #     return instance