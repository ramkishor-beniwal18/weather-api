from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from django.core.exceptions import ObjectDoesNotExist

from .models import Record
from .serializers import RecordSerializer


class RecordWeatherView(APIView):
    def post(self, request):
        serializer = RecordSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(data=serializer.data, status=status.HTTP_201_CREATED)

    def get(self, request, id=None):
        if id:
            try:
                item = Record.objects.get(id=id)
            except ObjectDoesNotExist as e:
                return Response(status=404)
            else:
                serializer = RecordSerializer(item)
                return Response(data=serializer.data, status=status.HTTP_200_OK)

        items = Record.objects.all()
        if items:
            serializer = RecordSerializer(items, many=True)
            return Response(data=serializer.data, status=status.HTTP_200_OK)
        else:
            return Response(status=404)

    def delete(self, request, id=None):
        try:
            item = Record.objects.get(id=id)
        except ObjectDoesNotExist as e:
            return Response(status=404)
        else:
            item.delete()
            return Response(status=204)
