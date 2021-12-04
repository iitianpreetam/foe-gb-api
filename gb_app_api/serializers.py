from rest_framework import serializers
from gb_app.models import GreatBuilding, GBLevel

class GBLevelSerializer(serializers.ModelSerializer):
    # gb_name = serializers.SerializerMethodField()
    class Meta:
        model = GBLevel
        fields = '__all__'

class GreatBuildingSerializer(serializers.ModelSerializer):
    levels = serializers.SerializerMethodField(read_only=True)
    class Meta:
        model = GreatBuilding
        fields = '__all__'

    def get_levels(self, obj):
        level = obj.gb_level
        serializer = GBLevelSerializer(level, many=True)
        return serializer.data