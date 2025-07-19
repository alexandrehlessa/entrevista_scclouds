def nums_primos(n):
    lista_nums_primos = []
    n = n + 1
    for i in range(2, n):
        is_primo = True
        for x in range(2, int(i/2 + 1)):
            if i % x == 0:
                #print(f"{i} não primo")
                is_primo = False
                break

        if is_primo == True:
          #print(f"{i} primo")
          lista_nums_primos.append(i)
    return lista_nums_primos
        



while(True):
        try:
            num = int(input("Digite o número máximo: "))
            if num >= 2:
                lista_nums_primos = nums_primos(num)
                print(f"p({num}) = {lista_nums_primos}")
                break
            else:
                print("Escreva um número igual ou maior que 2")
        except ValueError:
            print("Digite um número válido")


