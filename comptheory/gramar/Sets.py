import numpy as np
import re

#1. Operações com Alfabetos e Palavras

#Problema: Implemente um programa que realiza as operações de união, intersecção e diferença de conjuntos entre alfabetos e palavras.
#Contexto Teórico: A base de qualquer linguagem formal são os alfabetos (conjuntos de símbolos) e as palavras (sequências finitas de símbolos). Operações de conjuntos são fundamentais para manipular esses elementos.

#Tarefa:
#    Crie duas funções: uniao_conjuntos(conjunto1, conjunto2) e intersecao_conjuntos(conjunto1, conjunto2) que recebam listas de strings e retornem o resultado das respectivas operações.
#    Demonstre o uso com dois alfabetos: A = {'a', 'b', 'c'} e B = {'b', 'c', 'd', 'e'}.

#10. Verificação de Subconjunto e Subconjunto Próprio

#Problema: Crie um programa para verificar se um conjunto é subconjunto de outro, e se é um subconjunto próprio.
#Contexto Teórico: Na teoria dos conjuntos, X é um subconjunto de Y se todos os elementos de X também estão em Y. É um subconjunto próprio se 
#X é subconjunto de Y e X não é igual a Y.


#Tarefa:
#    Implemente uma função eh_subconjunto(A, B) e eh_subconjunto_proprio(A, B).
#    Use conjuntos como set do Python para resolver o problema de forma eficiente.
#    Teste com os conjuntos X = {1, 2}, Y = {1, 2, 3} e Z = {1, 2}. Verifique a relação entre X e Y, e entre X e Z.

class Grammar:
    def __init__(self):
        ""

    def operations():
        "Operações com conjuntos"

        title = "### - Calculadora de Conjuntos - ###"
        print(f"{title}") 

        set1 = {'a','b','c'}
        set2 = {'b','c','d','e'}
        result = {}
        
        print("Uniao: ",set1.union(set2))

        print("Intersecçao: ",set1.intersection(set2))

        print("Diference: ",set1.difference(set2))

        print("Subconjunto: ",set1.issubset(set2))

        print("Conjunto propio: ",set1<set2)
        
Grammar.operations()

