import xmlrpc.client


proxy = xmlrpc.client.ServerProxy("http://server:8000/RPC")
print("Cliente conectado ao servidor.")


def exibir_menu():
    print("\n--- Calculadora Remota XML-RPC ---")
    print("Escolha uma operação:")
    print("1. Somar (add)")
    print("2. Subtrair (sub)")
    print("3. Multiplicar (mult)")
    print("4. Dividir (div)")
    print("5. Potência (pow)")
    print("6. Raiz Quadrada (sqrt)")
    print("7. Módulo (mod)")
    print("8. Ordenar uma lista (sort)")
    print("9. Game Adivinhe um numero")
    print("Digite 'sair' para encerrar.")
    print("------------------------------------")

while True:
    exibir_menu()
    escolha = input("Opção: ")

    if escolha.strip().lower() == 'sair':
        print("Encerrando o cliente.")
        break

    try:
        if escolha == '1': # Somar
            x = float(input("Digite o primeiro número: "))
            y = float(input("Digite o segundo número: "))
            resultado = proxy.add(x, y)
            print(f"Resultado: {resultado}")

        elif escolha == '2': # Subtrair
            x = float(input("Digite o primeiro número: "))
            y = float(input("Digite o segundo número: "))
            resultado = proxy.sub(x, y)
            print(f"Resultado: {resultado}")

        elif escolha == '3': # Multiplicar
            x = float(input("Digite o primeiro número: "))
            y = float(input("Digite o segundo número: "))
            resultado = proxy.mult(x, y)
            print(f"Resultado: {resultado}")

        elif escolha == '4': # Dividir
            x = float(input("Digite o dividendo: "))
            y = float(input("Digite o divisor: "))
            resultado = proxy.div(x, y)
            print(f"Resultado: {resultado}")

        elif escolha == '5': # Potência
            base = float(input("Digite o número da base: "))
            expoente = float(input("Digite o expoente: "))
            resultado = proxy.pow(base, expoente)
            print(f"Resultado: {resultado}")

        elif escolha == '6': # Raiz Quadrada
            num = float(input("Digite o número para calcular a raiz quadrada: "))
            resultado = proxy.sqrt(num)
            print(f"Resultado: {resultado}")
            
        elif escolha == '7': # Modulo
            x = float(input("Digite o dividendo: "))
            y = float(input("Digite o divisor: "))
            resultado = proxy.mod(x, y)
            print(f"Resto: {resultado}")

        elif escolha == '8': # Ordenar
            lista_str = input("Digite os números para ordenar, separados por espaço: ")
            numeros = [float(n) for n in lista_str.split()]
            resultado = proxy.sort(numeros)
            print(f"Lista ordenada: {resultado}")
            
        elif escolha == '9': # jogo adivinhe o numero
            numero = int(input("Adivinhe o numero da vez: "))
            print("DICA: Um numero inteiro, positivo e diferente de 0")

            resultado = proxy.adv(numero)
            if resultado == numero:
                print(f"Voce acertou o numero supresa e: {resultado}")
            else:
                print(f"Voce errou o numero supresa e: {resultado}")

        else:
            print("Opção inválida. Tente novamente.")

    except ValueError:
        print("Erro: Entrada inválida. Por favor, digite apenas números.")
    except xmlrpc.client.Fault as f:
        print(f"Erro retornado pelo servidor: {f.faultString}")
    except Exception as e:
        print(f"Ocorreu um erro inesperado: {e}")