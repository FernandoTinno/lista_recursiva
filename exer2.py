'''
Exercício 2: Soma de Números em uma Lista Aninhada
Implemente uma função recursiva chamada soma_lista_aninhada(lista) que calcula a
soma de todos os números em uma lista, mesmo que os números estejam dentro de
sublistas (listas aninhadas).
Exemplo de Entrada:
soma_lista_aninhada([1, [2, 3], [4, [5]]])
Saída Esperada:
15 # (1 + 2 + 3 + 4 + 5)
Dica: Verifique se o elemento atual é uma lista ou um número para decidir se deve
continuar a recursão.
'''

def soma_lista_aninhada(lista):

    soma = 0
    for num in lista:
        if isinstance(num, list):#delimitar um valor de uma variavel ou uma variavel, como um tipo especeficico,aqui por exemplo é uma condicional para saber se o elemento em si é uma lista
            soma += soma_lista_aninhada(num)#retorna a função mas usando o elemento como um valor unico,deixando de ser uma lista e se tornando um numero aparte 
            
        elif isinstance(num, (int, float)):#checar se o valor escolhido é interio ou real 
            soma += num #incrementar o valor para uma variavel
              
    return soma


lista_exemplo = [1, [2, 3], [4, [5]]]
resultado = soma_lista_aninhada(lista_exemplo)
print(f"A soma dos números na lista é: {resultado}")  