# Trabalho T1 - Erros em Aproximações numéricas

### MTM 224 - Métodos Numéricos Computacionais
### Eng. Química(305) - Turma 14

*Nome*: Gabriel Righi

*Matrícula*: 201612819

---
## Questão 1
Pesquise e responda: O que é o *Épsilon da Máquina*? Apresente um programa em
python para obter o épsilon do computador que você usa. Qual o valor obtido com
seu programa?

###### Resposta:
Épsilon da máquina é o menor número que somado a 1 produza resultado diferente de 1.
Devido a limitação de memória que podemos representar com a quantidade de bits disponíveis
em um _Float_ , existe um número tão pequeno que causa um _Erro_ de arredondamento, de forma
que é representado pela letra grega "ε".

---
Questão 2
Use um progama em Python para realizar a soma  𝑆1=1000+∑10000𝑛=00.1  e a soma  𝑆2=∑10000𝑛=00.1+1000 . Compare os resultados e comente.

###### Resposta:
A diferença de valores se dá pelo fato que o computador não consegue representar certos números de forma exata, ocorrem diferenças
devido aos bits utilizados ao somar números muito pequenos com números muito grandes, o que cria essa discrepância entre os valores.
Enquanto S1 soma 1000 com o valor de $x$ que foi definido pela soma consecutiva no laço _for_ , o valor se faz diferente em S2, onde
soma-se 0.1 a um número muito grande, no caso 1000.

---
## Questão 3
Considere as expressões:
$\frac{e^{\frac{1}{x}}}{1 + e^{\frac{1}{x}}}$  e  $\frac{1}{e^{\frac{1}{x}} + 1}$. Verique que,
para $x$ > 0, são funções idênticas, então, use um programa em Python para testar o valor de cada uma para alguns valores
de $x$ entre 0.1 e 0.001. Qual. dessas expressões é mais adequada quando x é um número pequeno? Explique.

###### Resposta:
Como é possível verificar, quando $x$ é um número pequeno, a precisão da segunda equação é muito superior, visto que na primeira
equação, o sistema reconhece o valor apenas como 1.0. O mais provável de se afirmar é que a primeira equação trabalha com a soma
números tão pequenos com números grandes de modo que o computador não reconhece e acaba "arredondando", de forma que o valor que
deveria variar em 1.0 não é representado.

---
## Questão 4
A fórmula de Leibniz para o número $\pi$ é dada pela série infinita $\frac{\pi}{4} = \sum_{n = 0}^{\infty} \frac{(-1)^{n}}{2n+1}$.
Apresente um programa em Python para obter uma aproximações para $\pi$ usando 50 termos da série. Calcule os erros absoluto e relativo.

## Questão 5
O método "divida e faça a média", um método antigo para aproximar a raiz quadrada
de qualquer número positivo $a$, pode ser formulado por $x_{i+1} = \frac{x_{i} + \frac{a}{x_{i}}}{2}$.
Faça um programa para calcular $\sqrt7$ com erro relativo inferior a ${10}^{-5}$.

**OBS**: O valor do erro absoluto como podemos ver, de fato é inferior a ${10}^{-5}$, porém por ser um número pequeno, o computador
reconheceu apenas como 0 absoluto, mas se compararmos manualmente, é possível ver a distinção de valores.
© 2019 GitHub, Inc.
