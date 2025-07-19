def fibonacci():
    lista_fibonacci_nums = []
    fibonacci_num_atual = 0
    fibonacci_num_soma = 1
    while(True):
        try:
            fibonacci_sequencia = int(input("Digite quantas sequências deseja: "))
            if fibonacci_sequencia >= 0:
                #print("numero ok")
                i =  0
                while (i <= fibonacci_sequencia):
                    lista_fibonacci_nums.append(fibonacci_num_atual)
                    #print(fibonacci_num_atual)                    
                    fibonacci_num_atual = fibonacci_num_atual + fibonacci_num_soma
                    fibonacci_num_soma = fibonacci_num_atual - fibonacci_num_soma
                    #print(i)
                    i = i + 1

                return lista_fibonacci_nums
            else:
                print("Escreva um número igual ou maior que 0")
        except ValueError:
            print("Digite um número válido")
         

lista_nums_fibonacci = fibonacci()
for i in range(0, len(lista_nums_fibonacci)):
            print (f"fib({i}) = {lista_nums_fibonacci[i]}") 