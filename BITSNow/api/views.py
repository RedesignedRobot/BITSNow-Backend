from datetime import date, timedelta, datetime

from rest_framework import generics
from .serializers import ItemSerializer
from .models import Items


class ItemView(generics.ListAPIView):
    queryset = Items.objects.all().order_by('eStartDate')
    serializer_class = ItemSerializer


class ItemCreateView(generics.CreateAPIView):
    serializer_class = ItemSerializer

    def perform_create(self, serializer):
        serializer.save()


class ItemDestroyView(generics.DestroyAPIView):
    serializer_class = ItemSerializer

    def perform_destroy(self, serializer):
        serializer.save()