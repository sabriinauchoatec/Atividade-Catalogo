from django.shortcuts import render, get_object_or_404
from .models import Catalogo

# Create your views here.
def lista_produtos(request):
    produtos = Catalogo.objects.all()
    return render(request, 'catalogo/lista_produtos.html', {'produtos': produtos})

def detalhe_produto(request, id):
    produto = get_object_or_404(Catalogo, id=id)
    context = {'catalogo': Catalogo}
    return render(request, 'catalogo/detalhe_produto.html',context)