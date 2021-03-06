import heapq
from typing import Text
import nltk
from nltk.tokenize import word_tokenize
from nltk.stem import RSLPStemmer
from nltk.cluster.util import cosine_distance
import re

def Processamento(Texto): #Formatar documentação (Retorna uma Lista com as palavras formatadas)
        numero = r'[0-9]'
        stemmer = RSLPStemmer()
        stopwords = nltk.corpus.stopwords.words('portuguese')
        TextoSemNumero = [data for data in Texto if not data.isdigit()] # remover numeros
        TextoPreFormatado = [data for data in TextoSemNumero if data not in stopwords] # remover stopwords    
        for i in range (len(TextoPreFormatado)):
                TextoPreFormatado[i] = TextoPreFormatado[i].lower() #letra minuscula             
                TextoPreFormatado[i] = TextoPreFormatado[i].rstrip('s') #remover plural
                if TextoPreFormatado[i][-1] == 'a':                        
                        TextoPreFormatado[i] = TextoPreFormatado[i][:-1] + "o" #deixar palavras no masculino
                TextoPreFormatado[i] = re.sub(r'[^\w]', '', TextoPreFormatado[i]) # remover pontuações
                if len(TextoPreFormatado[i]) >= 3: 
                         TextoPreFormatado[i] = stemmer.stem(TextoPreFormatado[i]) #Radical da Palavra
        TextoFormatado = []
        for palavra in TextoPreFormatado:
                if palavra.strip() and len(palavra) >3 : #Remover espaços em brancos e palavras com tamanho menor que 3
                        TextoFormatado.append(palavra)
        #print(TextoFormatado)
        return TextoFormatado

def Tokenizacao(Arquivos): # Tokenizacao de todos os Documentos
        Tokens = {}
        for documento in Arquivos:
                Texto = word_tokenize(documento.text) #Tokenizar conteudo
                Tokens[documento.text] = Processamento(Texto)
        return Tokens