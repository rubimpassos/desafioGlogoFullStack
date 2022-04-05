from rest_framework import generics

from .models import Food
from .serializers import FoodSerializer


class FoodAPIListView(generics.ListAPIView):
    queryset = Food.objects.all()
    serializer_class = FoodSerializer
