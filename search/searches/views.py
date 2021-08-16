from django.shortcuts import render
from searches.functions import tratarBusca

def index(request):
  return render(request, 'searches/index.html')

def results(request): 
  busca = request.GET.get('busca')
  context = tratarBusca.main(busca)
  print('teste', context, '\n')
  return render(request, 'searches/results.html', {'context': context})