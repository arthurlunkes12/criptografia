from django.urls import path
from Criptografia.views import (
    criptografar_view,
    descriptografar_view,
)

urlpatterns = [
    path('criptografar/', criptografar_view, name='criptografar'),
    path('descriptografar/',
         descriptografar_view,
         name='descriptografar'),
]
