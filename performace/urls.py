"""performace URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from editora.urls import editora_router
from escritor.urls import escritor_router
from livro.urls import livro_router

urlpatterns = [
    path('admin/', admin.site.urls),
    path('editora/', include(editora_router.urls)),
    path('escritor/', include(escritor_router.urls)),
    path('livro/', include(livro_router.urls)),
]
