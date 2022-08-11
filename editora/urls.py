from rest_framework import routers
from .views import EditoraViewSet

editora_router = routers.SimpleRouter()
editora_router.register(r'', EditoraViewSet)
