# Calculadora Simples

#num1, num2, op, result

num1   = 0
num2   = 0
result = 0
op     = ""

# Loop infinito para continuar pedindo entradas até que o usuário decida sair

while True:
    num1 = float(input("Digite o primeiro número: ")) # ler o primeiro numero
    op   = input("Digite a operação (+, -, *, /): ") # ler a operação desejada
    num2 = float(input("Digite o segundo número: ")) # ler o segundo numero

# Condições para verificar a operação desejada e realizar o cálculo correspondente

    if op == '+':
        result = num1 + num2
    elif op == '-':
        result = num1 - num2
    elif op == '*':
        result = num1 * num2
    elif op == '/': # Verifica se o segundo número é zero antes de realizar a divisão
        try:
            result = num1 / num2
        except ZeroDivisionError: # Tratamento de exceção para divisão por zero
            print("Erro: Divisão por zero não é permitida.")
            continue
        result = num1 / num2
    else:
        print("Operação inválida!")
        continue 
    print('{} {} {} = {}'.format(num1, op, num2, result))
