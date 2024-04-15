import re

def menu():
    back_menu = 's'
    while back_menu == 's':
        option = input('''
            ================================================
                        Agenda em Python
            MENU:
            
            [1] - CADASTRAR CONTATO 
            [2] - LISTAR CONTATOS
            [3] - DELETAR CONTATO 
            [4] - BUSCAR PELO NOME
            [5] - ATUALIZAR CONTATO            
            [6] - SAIR\n         
            Escolha uma opção: ''')
        
        if option=='1':
            add_contact()
        elif option=='2':
            list_contact()
        elif option=='3':
            del_contact()
        elif option == '4':
            search_contact()
        elif option =='5':
            att_contact()    
        else:
            out()   
        back_menu = input('Deseja voltar ao menu principal ? (s/n)  '.lower())                                          

def add_contact():
    print('   ***Adicionar Contato***\n')
    idcontact= input('Escolha o ID do seu contato:  ')
    name= input('Escolha o nome do seu contato:  ')
    telephone= input('Digite o telefone do contato:  ')
    email= input ('Digite o email do contato atualizado:   ')
    try:
        calendar = open('agenda.txt','a')
        data = f'ID: {idcontact}| Nome: {name} | Telefone: {telephone} | Email: {email} \n'
        calendar.write(data)
        calendar.close()
        print(f'\nContato Adicionado com Sucesso!\n')
    except:
        print('Erro na gravação do contato!')

def att_contact():
    print(f'   ***Atualizar Contato***   ')
    name_delete = input('Digite o nome para atualizar:  ').lower()
    calendar= open('agenda.txt','r')
    aux = []
    aux2 = []
    for i in calendar:
        aux.append(i)
    for i in range(0,len(aux)):
        if name_delete not in aux[i].lower():
            aux2.append(aux[i])  
    calendar= open('agenda.txt','w')        
    for i in aux2: 
            calendar.write(i)     
    print('   ***Atualizar Contato!***\n')
    idcontact= input('Escolha o ID do seu contato atualizado:  ')
    name= input('Escolha o nome do seu contato atualizado:  ')
    telephone= input('Digite o telefone do contato atualizado:  ')
    email= input ('Digite o email do contato atualizado:   ')
    try:
        calendar = open('agenda.txt','a')
        data = f'ID: {idcontact}| Nome: {name} | Telefone: {telephone} | Email: {email} \n'
        calendar.write(data)
        calendar.close()
        print(f'\nContato Atualizado com Sucesso!\n')
    except:
        print('Erro na gravação do contato!')


def list_contact():
    print(f'  ***Listar Contato***')
    calendar = open('agenda.txt','r')
    for contato in calendar:
        print(contato)
    calendar.close()
 

def del_contact():
    print(f'   ***Deletar Contato***   ')
    name_delete = input('Digite o nome para deletar:  ').lower()
    calendar= open('agenda.txt','r')
    aux = []
    aux2 = []
    for i in calendar:
        aux.append(i)
    for i in range(0,len(aux)):
        if name_delete not in aux[i].lower():
            aux2.append(aux[i])  
    calendar= open('agenda.txt','w')        
    for i in aux2:
        calendar.write(i)
    print(f'Contato deletado com sucesso!\n')
    list_contact()
    

def search_contact():
    name= input('Digite o nome a ser procurado: ').upper()
    print(f'   ***Buscar Contato***   ')
    calendar = open('agenda.txt','r')
    for contato in calendar:
        if name in contato.split('|')[1].upper():
            print(contato)
    calendar.close()

def out():
    print('Obrigado por utilizar!')
    print('Projeto Pedro Python Agenda\n", "***Best regards!***\n')
    exit()


def main():
    menu()

main()


