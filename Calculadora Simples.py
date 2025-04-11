# Calculadora Simples

#num1, num2, op, result

num1   = 0
num2   = 0
result = 0
op     = ""

while True:
    num1 = float(input("Digite o primeiro número: ")) # ler o primeiro numero
    op   = input("Digite a operação (+, -, *, /): ") # ler a operação desejada
    num2 = float(input("Digite o segundo número: ")) # ler o segundo numero

    if op == '+':
        result = num1 + num2
    elif op == '-':
        result = num1 - num2
    elif op == '*':
        result = num1 * num2
    elif op == '/':
        result = num1 / num2
    else:
        print("Operação inválida!")
        continue 
    print('{} {} {} = {}'.format(num1, op, num2, result))