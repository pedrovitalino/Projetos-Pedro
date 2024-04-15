from keywords import keyword

List_keys = []
chances = 5
win = False

 

while True:
#Criando a logica do jogo 
    
    for key in keyword:
        if key.lower() in List_keys:
           print(key,end=" ")
        else:
           print("_", end=" ")
    print(f"\n Você tem {chances} chances")

    key_user= input("Escolha uma letra para adivinhar:  ")     
    List_keys.append(key_user.lower())

    if key_user.lower() not in keyword.lower():
        chances -= 1 
    win = True
    for key in keyword: 
         if key.lower() not in List_keys:
            win = False

    if chances == 0 or win :
        break    


if win: 
        print(f'Parabéns, você ganhou! A palavra era: {keyword}')
else:
        print(f'Você perdeu! A palavra era: {keyword}')


