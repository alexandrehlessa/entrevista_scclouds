def fibonacci(n, fibonacci_num_atual=0, fibonacci_num_soma=1, i = 0, lista_nums_fibonacci=[]):
     
    lista_nums_fibonacci.append(fibonacci_num_atual)
    i = i + 1

    fibonacci_num_atual = fibonacci_num_atual + fibonacci_num_soma
    fibonacci_num_soma = fibonacci_num_atual - fibonacci_num_soma

    if i >= n+1:
        for i in range(0, len(lista_nums_fibonacci)):
            print (f"fib({i}) = {lista_nums_fibonacci[i]}") 
        return lista_nums_fibonacci

    return fibonacci(n, fibonacci_num_atual, fibonacci_num_soma, i, lista_nums_fibonacci)


while(True):
        try:
            fibonacci_sequencia = int(input("Digite quantas sequências deseja: "))
            if fibonacci_sequencia >= 0:
                fibonacci(fibonacci_sequencia)
                break
            else:
                print("Escreva um número igual ou maior que 0")
        except ValueError:
            print("Digite um número válido")