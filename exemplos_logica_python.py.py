"""
Arquivo: exemplos_logica_python.py
Descrição: Este arquivo contém exemplos simples de lógica de programação em Python,
ideal para iniciantes. Todos os exemplos estão comentados para facilitar o aprendizado.
"""

# 1. Mostrar "Olá, Mundo!"
print("Olá, Mundo!")

# 2. Somar dois números
num1 = int(input("Digite o primeiro número: "))
num2 = int(input("Digite o segundo número: "))
soma = num1 + num2
print("A soma é:", soma)

# 3. Verificar se um número é positivo ou negativo
numero = int(input("Digite um número: "))
if numero > 0:
    print("O número é positivo.")
elif numero < 0:
    print("O número é negativo.")
else:
    print("O número é zero.")

# 4. Contar de 1 a 10 usando um laço
for i in range(1, 11):
    print(i)

# 5. Pedir um nome e dizer "Olá"
nome = input("Digite seu nome: ")
print("Olá,", nome, "seja bem-vindo!")

# 6. Multiplicar dois números
num1 = int(input("Digite um número: "))
num2 = int(input("Digite outro número: "))
resultado = num1 * num2
print("O resultado da multiplicação é:", resultado)

# 7. Verificar se um número é par ou ímpar
numero = int(input("Digite um número: "))
if numero % 2 == 0:
    print("O número é par.")
else:
    print("O número é ímpar.")

# 8. Mostrar os números de 1 a 5 usando um laço
for i in range(1, 6):
    print(i)

# 9. Calcular o dobro de um número
numero = int(input("Digite um número: "))
dobro = numero * 2
print("O dobro do número é:", dobro)

# 10. Somar todos os números de 1 a 10
soma = 0
for i in range(1, 11):
    soma += i
print("A soma dos números de 1 a 10 é:", soma)

# 11. Converter temperatura de Celsius para Fahrenheit
celsius = float(input("Digite a temperatura em Celsius: "))
fahrenheit = (celsius * 9/5) + 32
print("A temperatura em Fahrenheit é:", fahrenheit)

# 12. Calcular a área de um quadrado
lado = float(input("Digite o tamanho do lado do quadrado: "))
area = lado ** 2
print("A área do quadrado é:", area)

# 13. Criar uma senha simples e verificar se está correta
senha_correta = "1234"
senha_digitada = input("Digite a senha: ")
if senha_digitada == senha_correta:
    print("Acesso permitido!")
else:
    print("Senha incorreta!")

# 14. Contagem regressiva de 5 até 1
for i in range(5, 0, -1):
    print(i)
print("Fim da contagem!")

# 15. Verificar se um número está entre 10 e 20
numero = int(input("Digite um número: "))
if 10 <= numero <= 20:
    print("O número está entre 10 e 20.")
else:
    print("O número está fora do intervalo.")
