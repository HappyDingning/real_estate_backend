from django.db import transaction

from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response

from token_info.models import RealEstateBaseInfo
from token_info.serializers import RealEstateBaseInfoSerializer
from real_estate_backend.token_settings import image_tmp_bucket

class RealEstateBaseInfoAPIView(APIView):
    @transaction.atomic
    def post(self, request):
        serializer = RealEstateBaseInfoSerializer(data=request.data)

        if serializer.is_valid():
            real_estate_base_info = RealEstateBaseInfo(
                name=serializer.validated_data['name'],
                description=serializer.validated_data.get('description', ''),
                creator=serializer.validated_data['creator'],
            )

            real_estate_base_info.save()

            image_tmp_bucket.put_object("%d.jpg" % real_estate_base_info.id, request.data["image"])

            return Response(status=status.HTTP_204_NO_CONTENT)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
