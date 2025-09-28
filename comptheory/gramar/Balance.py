import numpy as np

#4. Validação de Parênteses Balanceados (Linguagem Livre de Contexto)
#Problema: Escreva um validador para expressões que contenham parênteses balanceados, como (()()) ou (()).
#Contexto Teórico: O balanceamento de parênteses é um problema clássico que não pode ser resolvido por um AFD, pois exige memória para "contar" os parênteses abertos. Ele pertence à classe das linguagens livres de contexto e é comumente resolvido com uma pilha, o que é análogo a um Autômato com Pilha.


#Tarefa:
#    Implemente uma função check_balance(expressao) que utiliza uma pilha (lista em Python) para verificar o balanceamento.
#    Para cada parêntese de abertura (, adicione um item à pilha. Para cada parêntese de fechamento ), remova um item da pilha. Se a pilha ficar vazia antes de um fechamento, ou se houver itens sobrando no final, a expressão é inválida.

class Balance:
    def __init__(self):
        pass

    