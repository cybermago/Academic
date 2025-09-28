import numpy as np
#8. Reconhecimento de Palíndromos
#Problema: Verifique se uma string é um palíndromo (aabbaa).
#Contexto Teórico: Palíndromos são uma linguagem livre de contexto, o que significa que um AFD não é capaz de reconhecê-los (ele não tem memória para "contar" e comparar o primeiro e o último caracteres).


#Tarefa:
#    Implemente uma função eh_palindromo(palavra) que verifica se a palavra é a mesma quando lida de trás para frente.
#    Resolva o problema sem usar o [::-1] do Python. Use um loop para comparar os caracteres da extremidade para o centro.

class Palindrome:
    def __init__(self):
        pass