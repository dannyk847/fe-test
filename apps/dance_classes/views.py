# Using Django Rest Framework to write Rest API endpoints
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from .business import create_dance_class
from .queries import query_all_dance_classes
from .serializers import DanceClassSerializer


class DanceClassCreateListAPIView(APIView):
    def get(self, request, *args, **kwargs):
        """
        Return all `DanceClass` records.
        """

        dance_classes = query_all_dance_classes()
        results = DanceClassSerializer(dance_classes, many=True).data
        return Response(results, status=status.HTTP_200_OK)

    def post(self, request, *args, **kwargs):
        """
        Create a `DanceClass` record.
        """

        serializer = DanceClassSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        result = create_dance_class(**serializer.validated_data)
        if not result.is_ok:
            raise result.unwrap_err()

        detail = result.unwrap()
        return Response(detail, status=status.HTTP_200_OK)
