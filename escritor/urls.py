from rest_framework import routers
from .views import EscritorViewSet

escritor_router = routers.SimpleRouter()
escritor_router.register(r'', EscritorViewSet)
