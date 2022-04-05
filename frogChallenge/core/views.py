from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import generics

from .filters import FoodFilter
from .models import Food
from .serializers import FoodSerializer


class FoodAPIListView(generics.ListAPIView):
    queryset = Food.objects.all()
    serializer_class = FoodSerializer
    filter_backends = (DjangoFilterBackend,)
    filterset_class = FoodFilter
