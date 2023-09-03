'''
Exercício numero 2 da lista de Exercícios realizada a criação do jogo de Jogo da velha no foramato nxn conforme específicação
deve ser informado ao iniciar o progama o tamanho do jogo da velha
para input é necessária a informação da posição da letra a ser colocada entre X e O nas quais caso possua 4 em sequencia em Coluna,linha ou diagonal retornara um vencedor

'''
import os
coluna = []
def tamanho_tabuleiro(tamanho):
    ''' Função que define o tamanho do tabulero sendo sempre um quadrado 4x4 - 5x5 - 6x6 - 7x7'''
    for i in range(0,tamanho):
        linha = []
        for j in range(0,tamanho):
            linha.append('-')
        coluna.append(linha)

def layout_tabuleiro():
    for i in range(0,len(coluna)):
        for j in range(0,len(coluna)):
            print(coluna[i][j] + " | ",end="") 
        print()

def adiciona_jogada(posicao_vertical,posicao_linha,sinbolo):
    '''Função que adiciona a jogada no jogo'''
    if (len(coluna) < posicao_vertical) or (len(coluna[0]) < posicao_linha): 
        raise Exception("Valor da posição vertical ou horizontal acima do esperado") 
    if coluna[posicao_vertical][posicao_linha] != '-':
       raise Exception("Posição já preenchida tente novamente")  
    coluna[posicao_vertical][posicao_linha] = sinbolo

def valida_jogo_ganho(coluna_vertical,linha):
    ''' Função em que é validado se quem venceu com a jogada '''
    def valida_linha(coluna_qualquer):
        return (all(x == 'X' for x in coluna[coluna_qualquer]) or all(x == 'O' for x in coluna[coluna_qualquer]))  
    
    def valida_coluna(index):
        return (all(x[index] == 'X' for x in coluna) or all(x[index] == 'O' for x in coluna))
    
    def valida_diagonal():
        return ((all(coluna[x][x] == 'X' for x in range(0,len(coluna))) or all(coluna[x][(len(coluna) - 1)-x] == 'X' for x in range(0,len(coluna))[::-1])) or (all(coluna[x][x] == 'O' for x in range(0,len(coluna))) or all(coluna[x][(len(coluna) - 1)-x] == 'O' for x in range(0,len(coluna))[::-1])))
    
    return (valida_linha(coluna_vertical)  or valida_coluna(linha) or valida_diagonal())

os.system('cls')
print("Jogo da velha")
print("Digite o tamanho do tabuleiro Ex: 10,3,5,7,8")
tamanho_tabuleiro(int(input()))
vencedor = "X"
vezJogador = False
countVelha =0
while True:
    print("Jogo da velha")
    layout_tabuleiro()
    if vezJogador:
        try:
            print("Digite onde queira marcar um X separado por virgula em (coluna,linha) Ex: 0,0 0,1 0,2")
            col,lin = [int(x) for x in input().split(",")]
            adiciona_jogada(int(col),int(lin),"X")
            vezJogador = not(vezJogador)
            if valida_jogo_ganho(int(col),int(lin)):
                break
        except Exception as e:
            print(e)
        else:
            os.system('cls')
    else:
        try:
            print("Digite onde queira marcar uma O separado por virgula em (coluna,linha) Ex: 0,0 0,1 0,2") 
            col,lin = [int(x) for x in input().split(",")]
            adiciona_jogada(int(col),int(lin),"O")
            vezJogador = not(vezJogador)
            if valida_jogo_ganho(int(col),int(lin)):
                vencedor = 'O'
                break
        except Exception as e:
            print(e)
        else:
            os.system('cls')
    if countVelha >= len(coluna):
        break
os.system('cls')
layout_tabuleiro()
if countVelha < len(coluna):
    print("O vencedor é o jogador que escolheu o Sínbolo "+vencedor)   
else:
    print("Deu Velha")
