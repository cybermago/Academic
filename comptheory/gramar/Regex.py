import numpy as np 
import re as re

#2. Validador de Expressão Regular
#Problema: Construa um programa que verifica se uma string de entrada pertence a uma linguagem definida por uma expressão regular simples.
#Contexto Teórico: Expressões Regulares (ER) são descritores poderosos para linguagens regulares. A aplicação prática mais comum é a validação de padrões.


#Tarefa:
#    Implemente uma função valida_er(string, padrao) que retorna True se a string corresponde ao padrao, e False caso contrário.
#    O padrão deve validar strings que contêm exatamente dois caracteres 'b' e terminam em 'a', sobre o alfabeto {a, b}. Por exemplo, "abba" e "bababa" são inválidos, mas "aba" e "bba" são válidos.
#    Use a biblioteca re do Python. Sua tarefa é traduzir a lógica formal para o uso prático da biblioteca.

class REGEX:
    def __init__(self):
        pass

    def valida_er(string, pattern):
            string = str(input(": "))
            pattern = re.search(r"bb{2}$a\w+", string)
            print(string == pattern)


REGEX.valida_er()