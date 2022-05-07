from rest_framework import serializers

from token_info.models import RealEstateBaseInfo


class RealEstateBaseInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = RealEstateBaseInfo
        fields = ('creator', 'name', 'description')
