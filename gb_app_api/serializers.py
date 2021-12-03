from rest_framework import serializers
from gb_app.models import GreatBuilding

class GreatBuildingSerializer(serializers.ModelSerializer):
    class Meta:
        model = GreatBuilding
        fields = '__all__'