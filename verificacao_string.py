entrada = input("Digite a frase a ser analisada: ")

def analise(str):
    a = ('a', 'A')
    contador = 0
    for i in str:
        if i in a:
            contador += 1

    return contador

numero = analise(entrada)


print("-"*42,"|")
if numero > 0:
    print(f'Há {numero} letra(s) A na frase analisada.')
else:
    print("Não há letras A na frase analisada.")