from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Dado

def validar_documento(request):
    error_message = ''
    codigo = request.POST.get('codigo', '').replace('-', '').strip()

    if request.method == 'POST':
        if codigo:
            try:
                dado = Dado.objects.get(codigo=codigo)
                # Salvar o código na sessão
                request.session['codigo'] = codigo
                return redirect('dadosDocumento')  # Problema ocorria aqui
            except Dado.DoesNotExist:
                messages.error(request, 'Erro, código verificador inexistente')
                return redirect(f'{request.path}?codigo={codigo}')
        else:
            error_message = 'Código verificador não pode estar vazio'

    context = {'codigo': codigo, 'error_message': error_message}
    return render(request, 'home.html', context)

def dados_documento(request):
    codigo = request.session.get('codigo')
    if not codigo:
        return redirect('validarDocumento')

    try:
        dado = Dado.objects.get(codigo=codigo)
        context = {'dado': dado}
        return render(request, 'dados.html', context)
    except Dado.DoesNotExist:
        messages.error(request, 'Usuário não encontrado')
        return redirect('validarDocumento')
