print('\nBem vindo ao Guess Par ou impar!!  \n')

numberg = int(input('Digite um número entre 1 e 1000:\n '))
result1 = numberg % 2

if numberg > 1000:
    print('Numero incorreto!\n')
    numberg1 = int(input('Digite um número entre 1 e 1000:\n '))
else:
    result1()

if result1 == 0 or numberg1 == 0:
    print(f'O número é par!')
else:
    print(f'o número é impar')





