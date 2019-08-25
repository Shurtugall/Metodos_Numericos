"""
@author: Gabriel Righi
@matricula: 201612819
"""
#Questão 4

import math

def main():
    
    pi = 0
    #Cálculo da variável pi
    for n in range(50):
        pi = pi + ((4.0*((-1)**n))/(2*n + 1))
        print(n+1,"º termo da serie: ", pi)
    
    #Cálculo do erro absoluto
    erro_absoluto = math.pi - pi
    print("\nErro absoluto: ", math.fabs(erro_absoluto))
    
    #Cálculo do erro relativo
    erro_relativo = erro_absoluto/(math.fabs(math.pi))
    print("Erro relativo: ", erro_relativo)
    
main()
