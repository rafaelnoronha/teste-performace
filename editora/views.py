from rest_framework import viewsets
from .models import Editora
from .serializers import EditoraSerializer


class EditoraViewSet(viewsets.ModelViewSet):
    queryset = Editora.objects.all()
    serializer_class = EditoraSerializer

