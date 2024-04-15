from time import sleep

class calculator():
    def add (a,b):
        add_= a + b
        print(a,'+',b, '=',add_)

    def sub (a,b):
        sub_ = a-b  
        print(a,'-',b, '=',sub_)  

    def plus(a,b):
        plus_ = a*b
        print(a,'*',b, '=',plus_)

    def div(a,b):
        div_ = a/b
        print(a,'/',b, '=',div_)


    print('Bem vindo a calculadora! \n')   

    while True:
        print(' Menu: \n')
        print(' [1] - Adição\n [2] - Subtração\n [3] - Multiplicação \n [4] - Divisão \n [5] Sair \n')
        choice= int(input('\n Seleciona a opção deseja: '))

        if choice == 1:
            a = int(input('Digite o primeiro valor:\n'))
            b = int(input('Digite o segundo valor:\n\n'))
            add(a,b)
            sleep(3)
        elif choice == 2:
            a = int(input('Digite o primeiro valor:\n'))
            b = int(input('Digite o segundo valor:\n\n'))
            sub(a,b)
            sleep(3)
        elif choice == 3:
            a = int(input('Digite o primeiro valor:\n'))
            b = int(input('Digite o segundo valor:\n\n'))
            plus(a,b)
            sleep(3)    
        elif choice == 4:
            a = int(input('Digite o primeiro valor:\n'))
            b = int(input('Digite o segundo valor:\n\n'))
            div(a,b)
            sleep(3)    
        elif choice == 5:
            print("Finalizando Programa!")
            break
