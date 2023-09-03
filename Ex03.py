'''
Exercício numero 3 da lista de Exercícios realizada a criação do jogo de  Teermo conforme específicação
O jogo irá escolher uma palavra de uma lista de palavras prédefinidas e mostrar o tamanho desta palavra
O jogo aceitará qualquer palabra que tenha o mesmo tamanho da palabra gerada automaticamente , após a tentativa do usuário serão destacados com cores as letras que demonsram acerto sendo:
Verde para uma letra certa na casa certa, amarelo para uma letra cetra no lugar errado e Deixando cinza para caso a letra não exista na palavra
Após n tentativas de acordo com o tamanho da palavra o jogo se encerra em derrota caso a a palavra não seja descoberta antes

'''

import os
import random
from unicodedata import normalize
class bcolors:
    HEADER = '\033[0m'
    YELLOW = '\033[93m'
    GREEN = '\033[32m'
    FRACO = '\033[90m'

arquivo = "lista_palavras.txt"
def le_arquivo(arq):
    """ Lê arquivo especificado e retorna uma lista com todas as linhas """    
    with open(arq, encoding="UTF-8") as f:
        return [linha.strip() for linha in f] # método strip remove o '\n' do final da linha
lista = le_arquivo(arquivo)  
#print(lista)   
lista_letras_utilizadas = []
lista_letras_lugar_incorreto = []
lista_letras_corretas = []
lista_letras_incorretas = []
''' remove ascentos'''
palavra_escolhida =  normalize('NFKD', str(random.choice(lista)).upper()).encode('ASCII','ignore').decode('ASCII') 
#print(palavra_escolhida) 
def valida_palavra(palavra_informada):
    """ Valida as palavras inseridas pelo usuário e preenche as listas de informações sobre acertos e erros""" 
    for i in range(0,len(palavra_escolhida)):
        if palavra_escolhida[i] == palavra_informada[i]:
            if not (palavra_informada[i] in lista_letras_corretas):
                lista_letras_corretas.append(palavra_informada[i])
                if palavra_informada[i] in lista_letras_lugar_incorreto:
                    lista_letras_lugar_incorreto.remove(palavra_informada[i])
        else:
            if palavra_informada[i] in palavra_escolhida:
                lista_letras_lugar_incorreto.append(palavra_informada[i])
            else:
                lista_letras_incorretas.append(palavra_informada[i])

def show_palavra(palavra_informada):
    """ Demonstra em tela a palavra do usuário com validações de cores conforme especificacao""" 
    print("-----------------------------------------------------")
    for i in range(0,len(palavra_escolhida)):
        if palavra_informada == '-1-1-1':
            print('|  |',end=" ")  
        else:
            if palavra_informada[i] == palavra_escolhida[i]:
                print(bcolors.GREEN + palavra_informada[i],end=" | ")
            else:
                if palavra_informada[i] in palavra_escolhida:
                    print(bcolors.YELLOW + palavra_informada[i],end=" | ")
                else:
                    print(bcolors.FRACO + palavra_informada[i],end=" | ") 
    print()
    print("-----------------------------------------------------")

def show_listas_palavras():
    """ Demonstra em tela o alfabeto e as letras disponiveis e acertos do usuário""" 
    letras = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    for i in letras:
        if i in lista_letras_corretas:
            print(bcolors.GREEN+ i,end=" | ")
        else:
            if i in lista_letras_lugar_incorreto:
                print(bcolors.YELLOW+ i,end=" | ") 
            else:
                if i in lista_letras_incorretas: 
                    print(bcolors.FRACO+ i,end=" | ")  
                else:
                    print(bcolors.HEADER+ i,end=" | ")     
print("           TERMO           ")
print("           "+str(len(palavra_escolhida))+" Letras            ")
show_palavra('-1-1-1')
contador = len(palavra_escolhida)
while True:
    try:
        print(bcolors.HEADER+'')
        palavra_info = input("Digite o Termo: ")
        if len(palavra_info) != len(palavra_escolhida):
            raise Exception('Tamanho do termo difere to tamanho da palavra escolhida')
        valida_palavra(palavra_info.upper())
        show_palavra(palavra_info.upper())
        show_listas_palavras()
        if palavra_escolhida == palavra_info.upper():
            print("")
            print("-----------------------------------------------------")
            print('Você Ganhou')
            print("-----------------------------------------------------")
            break
        contador -= 1
        if contador == 0:
            print("")
            print("-----------------------------------------------------")
            print('Você perdeu')
            print("A palavra gerada era: "+palavra_escolhida)
            print("-----------------------------------------------------")
            break

    except Exception as e:
        print(e)

    #show_palavra(palavra_info)
            






    
