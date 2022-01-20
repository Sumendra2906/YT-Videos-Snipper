from rest_framework import serializers
from .models import VideosInfo


class VideosInfoSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = VideosInfo
        fields = "__all__"