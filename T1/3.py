"""
@author: Gabriel Righi
@matricula: 201612819
"""
#Questão 3

import math

def main():
    
    x = 0.001
    for i in range(100):
        try:
            result1 = math.exp(1/x) / (1 + math.exp(1/x))
            print("Resultado da 1ª equação com x=", x, ":", result1)
        except OverflowError:
            print("Resultado da 1ª equação com x=", x, ": Não é possível representar(Overflow)")
            
        try:
            result2 = 1 / (math.exp(1/x) + 1)
            print("Resultado da 2ª equação com x=", x, ":", result2, "\n")
        except OverflowError:
            print("Resultado da 2ª equação com x=", x, ": Não é possível representar(Overflow)\n ")
            
        x = x + 0.001
        
    diff = result1 - result2    
    print("Fim do laço de repetição!\nResultado da diferença final: ", diff)

main()