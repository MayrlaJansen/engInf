from searches.functions import addDocs
from searches.functions import BagOfWord

# def buscar(busca):
#   docs = addDocs.testando()
#   # print( docs)
#   return docs

import math
from typing import Dict
from nltk.tokenize import word_tokenize
from nltk.cluster import cosine_distance
from operator import itemgetter

import numpy as np


def Token(Keys):  # Cria um map <Palavra,Peso>s
    Contador = {}
    for key in Keys:
        Contador[key] = 0
    return Contador


def computeTF(Vetor, BagOFWord):
    Resultado = []
    count = len(BagOFWord)
    for valor in Vetor:
        Resultado.append(valor / count)
    return Resultado


def computeIDF(BagOFWord, Arquivos):
    Resultado = {}
    for word in BagOFWord:
        Resultado[word] = math.log(len(Arquivos)/DocsComTermo(word, Arquivos))
    return Resultado


def DocsComTermo(Termo, Arquivos):
    count = 0
    for key, value in Arquivos.items():
        if Termo in value:
            count += 1
    return count


def computeTF_IDF(Vetor, BagOfWord, Arquivos):
    Resultado = []
    index = 0
    TF = computeTF(Vetor, BagOfWord)
    IDF = computeIDF(BagOfWord, Arquivos)
    for key, value in IDF.items():
        Resultado.append(TF[index] * value)
        index += 1
    return Resultado


def Similaridade(TokenPesquisa, Tokens, Arquivos):  # Calculo da Similaridade
    Chaves = list(TokenPesquisa.keys())  # Lista com as chaves da pesquisa
    # Lista com todas as palavras (Pesquisa + Documento)
    TodasPalavras = list(set(Chaves + Tokens))
    Vetor1 = [0] * len(TodasPalavras)
    Vetor2 = [0] * len(TodasPalavras)
    for palavra in Chaves:  # Calcular vetor de quantidade de termo para Chave
        Vetor1[TodasPalavras.index(palavra)] += 1
    for palavra in Tokens:  # Calcular vetor de quantidade de termo para Documento
        Vetor2[TodasPalavras.index(palavra)] += 1
    Vetor1 = computeTF_IDF(Vetor1, TodasPalavras, Arquivos)
    Vetor2 = computeTF_IDF(Vetor2, TodasPalavras, Arquivos)
    # print(Vetor1)
    # print(Vetor2)
    # print()
    return (cosine_distance(Vetor1, Vetor2))


def CossenoDistance(TokenPesquisa, Arquivos):
    Resultado = {}
    for key, value in Arquivos.items():
        Resultado[key] = Similaridade(TokenPesquisa, value, Arquivos)
    Ordenado = sorted(Resultado.items(), key=itemgetter(1))
    # print(Ordenado)
    return Resultado


def main(busca):
    Pesquisa = busca  # Valor que quero buscar
    PesquisaFormatada = BagOfWord.Processamento(
        word_tokenize(Pesquisa))  # Tokenizar e formatar busca
    TokenPesquisa = Token(PesquisaFormatada)
    Arquivos = addDocs.GetArquivos()  # Lista com Arquivos
    Tokens = BagOfWord.Tokenizacao(Arquivos)  # Map <Texto,Token>
    CossenoDistancia = CossenoDistance(TokenPesquisa, Tokens)

    return addDocs.PrintArquivosResultado(CossenoDistancia)
    


# if __name__ == '__main__':

#     main()
