from rest_framework import serializers
from apps_watchlist.models import Watchlist, StreamPlatform, Review


def len_title(value):
    if len(value)<2:
        raise serializers.ValidationError("Name is Two Short. It must be greator than 2")

def len_descriptions(value):
    if len(value)<30:
        raise serializers.ValidationError("Description is two short. It must be greater than 30 characters")

class ReviewSerializer(serializers.ModelSerializer):
    watchlist = serializers.HyperlinkedRelatedField(read_only=True, view_name='api:watchlist_detail')
    class Meta:
        model = Review
        fields = '__all__'


class WatchlistSerializer(serializers.ModelSerializer):
    title = serializers.CharField(validators=[len_title])
    descriptions = serializers.CharField(validators=[len_descriptions])
    platform = serializers.HyperlinkedRelatedField(read_only=True, view_name='api:stream_detail')#returns __str__ of streamplatform
    reviews = ReviewSerializer(many=True, read_only=True)
    class Meta:
        model = Watchlist
        fields = ['id','title','descriptions','type','platform','active','reviews', 'created','updated']
        

    # def create(self, validated_data):
    #     return Watchlist.objects.create(validated_data)
    
    # def update(self, instance, validated_data):
    #     instance.title = validated_data.get('title', instance.title)
    #     instance.descriptions = validated_data.get('descriptions', instance.descriptions)
    #     instance.active = validated_data.get('active', instance.active)
    #     instance.save()
    #     return instance


    # '''Field level validatoin we call a method with validate_<field>(self, value)'''
    # def validate_title(self, value):
    #     if len(value)<2:
    #         raise serializers.ValidationError("Name is too short")
    #     else:
    #         return value

    '''Object level validation we call a method to add logic to validate the data'''
    def validate(self, data):
        if data['title']==data['descriptions']:
            raise serializers.ValidationError("Title and description of Watchlist must not be same")
        else:
            return data


class StreamPlatformSerializer(serializers.ModelSerializer):
    #watchlist = WatchlistSerializer(many=True, read_only=True)
    watchlist = serializers.HyperlinkedRelatedField(many=True, read_only=True, view_name='api:watchlist_detail')
    class Meta:
        model = StreamPlatform
        fields = ['id','name','about','website','active', 'watchlist', 'created', 'updated']

    
