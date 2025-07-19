lista_nums_primos = []
def nums_primos(n, i = 1):
    i = i + 1
    num_atual_is_primo = True
    for x in range(2, int(i/2 + 1)):
        if i % x == 0:
            num_atual_is_primo = False
            #print(f"{i} nao é primo")
            break

    if num_atual_is_primo == True:
        #print(f"{i} é primo")
        lista_nums_primos.append(i)
        #print(lista_nums_primos)

    if i < n:
        #print(i)
        return nums_primos(n, i)
    
    if i >= n:
        return lista_nums_primos
    
    
while(True):
        try:
            num = int(input("Digite o número máximo: "))
            if num >= 2:
                lista_nums_primos = nums_primos(num)
                print(f"p({num}) = {lista_nums_primos}")
                break
            elif num == 1:
                print("Por regra e definição matemática (levando o pé da letra), o 1 não é primo, mas sempre foi uma angústia saber que o 1 é divisível apenas por 1 e por ele mesmo(1), porém já que temos que seguir as regras... Por favor, digite um número inteiro maior que 1")
            else:
                print("Escreva um número igual ou maior que 2")
        except ValueError:
            print("Digite um número válido")
