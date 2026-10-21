operacao = ["Soma", "Subtração", "Multiplicação", "Divisão"]

def menu(operacao, numero1, numero2):
    opcoes = [f"{i} - {opcao}" for i, opcao in enumerate(operacao, start=1)]
    print("\n".join(opcoes))
    try:
        escolha = int(input("Escolha uma operação (1-4): "))
        if escolha == 1:
                resultado = lambda numero1, numero2: numero1 + numero2
                print(f"O resultado da soma é: {resultado(numero1, numero2)}")
        elif escolha == 2:
                resultado = lambda numero1, numero2: numero1 - numero2
                print(f"O resultado da subtração é: {resultado(numero1, numero2)}")
        elif escolha == 3:
                resultado = lambda numero1, numero2: numero1 * numero2
                print(f"O resultado da multiplicação é: {resultado(numero1, numero2)}")
        elif escolha == 4:
            if numero2 == 0:
                    print("Erro: Divisão por zero não é permitida.")
                    return menu(operacao, numero1, numero2)
            else:
                    resultado = lambda numero1, numero2: numero1 / numero2
                    print(f"O resultado da divisão é: {resultado(numero1, numero2)}")
        if not escolha in range(1, 5):
            print("Opção inválida. Por favor, escolha uma operação válida.")
            return menu(operacao, numero1, numero2)
    except ValueError:
        print("Por favor, digite apenas números inteiros.")
        return menu(operacao, numero1, numero2)

def main():
    while True:
        while True:
            try:
                numero1 = int(input("Digite o primero número: "))
                numero2 = int(input("Digite o segundo número: "))
                break
            except ValueError:
                print("Por favor, digite apenas números inteiros.")

        menu(operacao, numero1, numero2)

        if input(str("Deseja realizar outra operação? S/N: ")).lower() == "s":
            continue
        print("Obrigado por usar a calculadora!")
        break

if __name__ == "__main__":
    main()
