#9. Geração de Fechamento de Kleene
#Problema: Gere as primeiras N palavras de uma linguagem definida pela operação de fechamento de Kleene (a+b)*.
#Contexto Teórico: A operação * (Fechamento de Kleene) sobre um alfabeto Σ gera todas as cadeias finitas, incluindo a cadeia vazia, que podem ser formadas com os símbolos de Σ.


#Tarefa:
#    Crie uma função gerar_fechamento_kleene(simbolos, n) que gere as primeiras n palavras da linguagem (a+b)*.
#    Comece com a cadeia vazia, depois palavras de comprimento 1, 2, e assim por diante.
#    A função deve retornar uma lista de strings.

class Klenne:
    def __init__(self):
        pass