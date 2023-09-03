'''
Exercício numero 4 da lista de Exercícios realizada a criação do banco de dados em dicionario conforme específicação
O usuário pode cadastrar diversos usuarios com campos que o mesmo informar e consultar de acordo com os filtros em tela
'''

banco_usuarios = {}

def cadastrar_usuario(campos):
    ''' Função que cadastra o usuário conforme campos obrigatorios e caso queira campos extras'''
    user = {}
    user["nome"] = input("Digite o valor para o campo nome: ")
    for i in range(0,len(campos)):
        valor = input("Digite o valor para o campo "+campos[i]+": ")
        user[campos[i]] = valor
    
    while True:
        campo_extra = input("Digite um campo extra ou 'Sair' para finalizar : ")
        if campo_extra.lower() == 'sair':
            break
        valor = input("Digite o valor para o campo  "+campo_extra+": ")
        user[campo_extra] = valor
    banco_usuarios[user["nome"]] = user
    print("Usuário cadastrado com sucesso!")
    
def produzir_filtro():
    ''' Função que produz o filtro de campos para a pesquisa e passar como parametro para outras funções'''
    filtro = {}
    while True:
        campo = input("Digite um campo para busca ou 'Sair' para finalizar : ")
        if campo.lower() == 'sair':
            break
        for nome,iteravel in banco_usuarios.items():
            if campo in iteravel:
                valor = input("Digite o valor para o campo  "+campo+": ")
                filtro[campo] = valor
                break
            else:
                print("Campo inexistente!")
    return filtro


def imprimir_usuarios(*args, **kwargs):
    ''' Função que Imprime os usuários de acordo com a seleção do menu'''
    print()
    if (len(args) == 0 and len(kwargs) == 0):
        for nome, i in banco_usuarios.items():
            print(i)

    if ((len(args) > 0) and (len(kwargs) == 0)) :   
        for nome, usuario in banco_usuarios.items():
           if any(nome == args[0][x] for x in range(0,len(args[0]))):
                print(usuario)    
                
    
    if ((len(args) == 0) and (len(kwargs) > 0)) :  
        campos = kwargs.keys() 
        for nome,usuario in banco_usuarios.items():
            if all(usuario.get(campo) == valor for campo, valor in kwargs.items()):
                print(usuario)  

    if ((len(args) > 0) and (len(kwargs) > 0)) :
        campos = kwargs.keys() 
        for nome,usuario in banco_usuarios.items():
            if (all(usuario.get(campo) == valor for campo, valor in kwargs.items()) and (any(nome == args[0][x] for x in range(0,len(args[0]))))):
                print(usuario)  

campos = input("Digite os nomes de campos obrigatórios para o cadastro, separação por virgula ").split(',')
while True:
    print("")
    print("Menu:")
    print("1 - Cadastrar usuário")
    print("2 - Imprimir usuários")
    print("0 - Encerrar")
    opcao = int(input("Escolha a opção: "))
    
    if opcao == 1:
        cadastrar_usuario(campos)
    elif opcao == 2:
        print("")
        print("Filtros de Usuários:")
        print("1 - impirmir todos")
        print("2 - filtrar por nomes")
        print("3 - filtrar por campos")
        print("4 - filtrar por nomes e campos")
        opcao_alter = int(input("Escolha a opção: "))
        match opcao_alter:
            case 1:
                imprimir_usuarios()
            case 2:
                nomes = input("Digite os nomes , separação por virgula: ").split(',')    
                imprimir_usuarios(nomes)
            case 3:
                imprimir_usuarios(**produzir_filtro())
            case 4:
                nomes = input("Digite os nomes , separação por virgula: ").split(',')    
                imprimir_usuarios(nomes,**produzir_filtro())
    elif opcao == 0:
        break
    else:
        print("Opção inválida!")