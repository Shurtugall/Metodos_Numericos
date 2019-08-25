"""
@author: Gabriel Righi
@matricula: 201612819
"""
#Questão 5
#duvida

import math

def main():
    a = 7
    x_ant = 0.1
    for i in range(10):
        x = (x_ant + a/x_ant)/2
        x_ant = x
        print("X", i+1, ":", x)
        
    erro_absoluto = math.sqrt(7.0) - x
    
    print("Erro absoluto: ", math.fabs(erro_absoluto))    
    
    
main()