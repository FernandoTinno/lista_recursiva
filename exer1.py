'''
Exercício 1: Reverter os Caracteres de uma String
Escreva uma função recursiva chamada reverter_caracteres(s) que recebe uma
string s e devolve a string invertida. Não use laços (for ou while).
'''

def word_inverter(word):
    if not word:  
        return word #testei o return word[0] ou qualquer outro index e dá erro de 'string index out of range' ou seja como está fora de alcançe, 
    #não existe nenhum valor nos index, o que não entendi seria, como não tendo valor algum, a palavra é mostrada ná tela mesmo assim?
    else:
        return word_inverter(word[1:]) + word[0] #pelo que entendi essa linha de codigo remove o primeiro caracter e adiciona ao final

word = 'roma'
print(word_inverter(word)) 

