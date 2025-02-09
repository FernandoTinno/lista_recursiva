'''
Exercício 3: Contar Caracteres em uma String
Crie uma função recursiva chamada contar_caracteres(s, c) que conta quantas vezes o
caractere c aparece na string s.
Exemplo de Entrada:
contar_caracteres("banana", "a")
Saída esperada:
3
'''

def contar_caracteres(s, c):
  
  if not s:
    return 0
  
  elif s[0] == c: 
    return  1+  contar_caracteres(s[1:], c)
  else:
    return contar_caracteres(s[1:], c)

print(contar_caracteres("banana", "a"))
