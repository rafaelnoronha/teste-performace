from rest_framework import routers
from .views import LivroViewSet

livro_router = routers.SimpleRouter()
livro_router.register(r'', LivroViewSet)
