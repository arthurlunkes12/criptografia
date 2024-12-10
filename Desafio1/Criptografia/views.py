from django.shortcuts import render
from .models import TextoCriptografado
from .utils import (
    criptografar_texto,
    descriptografar_texto,
    carregar_ou_gerar_chave)

CHAVE_CRIPTOGRAFIA = carregar_ou_gerar_chave()


def criptografar_view(request):
    if request.method == 'POST':
        texto = request.POST['texto']

        texto_criptografado = criptografar_texto(texto, CHAVE_CRIPTOGRAFIA)

        TextoCriptografado.objects.create(
            texto_original=texto,
            texto_criptografado=texto_criptografado
        )

        return render(request, 'resultado.html', {
            'texto_criptografado': texto_criptografado
        })

    return render(request, 'criptografar.html')


def descriptografar_view(request):
    if request.method == 'POST':
        texto_criptografado = request.POST['texto_criptografado']

        try:
            texto_original = descriptografar_texto(
                texto_criptografado,
                CHAVE_CRIPTOGRAFIA
                )
            return render(request, 'resultado.html', {
                'texto_original': texto_original
            })
        except Exception:
            return render(request, 'resultado.html', {
                'erro': 'Não foi possível descriptografar o texto.'
            })

    return render(request, 'descriptografar.html')
