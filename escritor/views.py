from .models import Escritor
from .serializers import EscritorSerializer
from rest_framework import viewsets


class EscritorViewSet(viewsets.ModelViewSet):
    queryset = Escritor.objects.all()
    serializer_class = EscritorSerializer
