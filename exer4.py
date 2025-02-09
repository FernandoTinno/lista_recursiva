'''
Escreva uma função recursiva chamada indice_maior_elemento(lista) que retorna o
índice do maior elemento em uma lista.
Exemplo de Entrada:
indice_maior_elemento([1, 5, 3, 9, 2])
Saída Esperada:
3 # O maior elemento é 9, que está no índice 3
'''




def indice_maior_elemento(lista):
    if not lista:  # Verifica se a lista está vazia
        return None  # Retorna None se a lista estiver vazia

    if len(lista) == 1:  # lista com apenas um numero
        return 0  # se tiver só um numero o indice sempre vai ser 0

    
    indice_resto = indice_maior_elemento(lista[1:])

    
    if lista[0] > lista[indice_resto + 1]:  # analisar se o primeiro valor da lista, é maior que os demais
        return 0  # Seu índice é 0
    else:  # se o index zero não é o maior, indica que o maior está no restante da lista
        return indice_resto + 1 # Ajusta o índice para o lugar certo em relação a lista original


print(indice_maior_elemento([1, 5, 3, 9, 2]))