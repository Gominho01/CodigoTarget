#Dado a sequência de Fibonacci, onde se inicia por 0 e 1 e o próximo valor sempre será a soma dos 2
# valores anteriores (exemplo: 0, 1, 1, 2, 3, 5, 8, 13, 21, 34...), escreva um programa na linguagem 
# que desejar onde, informado um número, ele calcule a sequência de Fibonacci e 
# retorne uma mensagem avisando se o número informado pertence ou não a sequência.

def is_fibonacci(n):
    a, b = 0, 1
    while b < n:
        a, b = b, a + b
    return b == n or n == 0

# Teste com um número informado
num = int(input("Digite um número: "))

if is_fibonacci(num):
    print(f"{num} pertence à sequência de Fibonacci.")
else:
    print(f"{num} NÃO pertence à sequência de Fibonacci.")
