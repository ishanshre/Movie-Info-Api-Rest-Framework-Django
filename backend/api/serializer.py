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


    '''Field level validatoin we call a method with validate_<field>(self, value)'''
    def validate_title(self, value):
        if len(value)<2:
            raise serializers.ValidationError("Name is too short")
        else:
            return value

    '''Object level validation we call a method to add logic to validate the data'''
    def validate(self, data):
        if data['title']==data['descriptions']:
            raise serializers.ValidationError("Title and description of movie must not be same")
        else:
            return data