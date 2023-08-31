coluna = []
def tamanho_tabuleiro(largura,altura):
    for i in range(0,altura):
        linha = []
        for j in range(0,largura):
            linha.append('-')
        coluna.append(linha)
tamanho_tabuleiro(13,10)
def adiciona_jogada(posicao_linha,posicao_vertical,sinbolo):
    if (len(coluna) < posicao_vertical) or (len(coluna[0]) < posicao_linha): 
        raise Exception("Valor da posição vertical acima do esperado") 
print(coluna[0])
print(len(coluna))

