from rest_framework import serializers
from rest_framework.response import Response
from gb_app.models import GreatBuilding
from .serializers import GreatBuildingSerializer
from rest_framework.decorators import api_view

@api_view(['GET'])
def get_gb(request):
    gbs = GreatBuilding.objects.all()
    serializers = GreatBuildingSerializer(gbs, many=True)
    return Response(serializers.data)