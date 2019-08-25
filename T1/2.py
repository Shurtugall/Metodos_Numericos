"""
@author: Gabriel Righi
@matricula: 201612819
"""
#Questão 2:

#Para S1:
def main():
    x = 0
    for n in range(10000):
        x = x + 0.1

    print('O resultado de S1 é:', 1000+x)
    
#Para S2:
    x = 1000
    for i in range(10000):
        x = x + 0.1
        
    print("O resultado de S2 é:", x)

main()