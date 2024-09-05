def fib(i, j, k):
    sequencia = [j, k]
    a = j
    b = k
    for i in range(2, i):
        a, b = b, a + b
        sequencia.append(b)
    return sequencia


try:
    entrada = int(input("Digite o número de elementos da sequência: "))

    print("-" * 75, "|")
    j = (input("Digite o primeiro elemento (Deixe vazio para a sequência padrão): "))
    numero_1 = int(j) if j else 0
    numero_2 = 1 if j == "" else int(input("Digite o segundo elemento: "))

    sequencia = fib(entrada, numero_1, numero_2)

    print("-" * 75, "|")
    print(f"Os {entrada} elementos da sequência são {sequencia}")
except ValueError:
    print("Digite um valor válido!")