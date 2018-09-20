##importando biblioteca pygame
import pygame
##biblioteca que pega um numero de um intervalo de numeros
from random import randint

##define as cores do jogo
branco =(255,255,255)
preto = (0,0,0)
vermelho = (255,0,0)
verde = (0,255,0)
azul = (0,0,255)
cinza = (209,209,209)

try:
    pygame.init()
except:
    print("O modulo pygame não foi inicializado com sucesso")
##define dimensões da tela, largura e altura
largura = 640
altura = 480
##define tamanho do objeto que desenhamos
tamanho = 10

##relogio que define fps
relogio = pygame.time.Clock()
##fundo do jogo com altura e largura
fundo = pygame.display.set_mode((largura,altura))
##nome que fica no topo da janela do jogo
pygame.display.set_caption("Jogo Snake")
pygame.font.SysFont(None,25)

def textos(msg, cor):
    texto1 = font.render(msg, True,cor)
    fundo.blit(texto1, [largura/2, altura/2])

##funcao que desenha a cobra
def cobra(cobraxy):
    for xy in cobraxy:
        pygame.draw.rect(fundo, verde, [xy[0],xy[1], tamanho, tamanho])
##funcao que desenha a maca
def maca(pos_x,pos_y):
    pygame.draw.rect(fundo, vermelho, [pos_x,pos_y, tamanho, tamanho])
##funcoes principais do jogo
def jogo():
    sair = True

    pos_x = randint(0,(largura-tamanho)/10)*10
    pos_y = randint(0,(altura-tamanho)/10)*10

    maca_x = randint(0,(largura-tamanho)/10)*10
    maca_y = randint(0,(altura-tamanho)/10)*10

    velocidade_x=0
    velocidade_y=0
    cobraxy = []
    cobracomp = 5
    while sair:
        for event in pygame.event.get():
            ##if para sair do jogo apertando o botao fechar        
            if event.type == pygame.QUIT:
                sair = False
            ##movimentos    
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT and velocidade_x != tamanho:
                    velocidade_y=0
                    velocidade_x=-tamanho
                if event.key == pygame.K_RIGHT and velocidade_x != tamanho:
                    velocidade_y=0
                    velocidade_x=tamanho
                if event.key == pygame.K_UP and velocidade_y != tamanho:
                    velocidade_x=0
                    velocidade_y=-tamanho
                if event.key == pygame.K_DOWN and velocidade_y != tamanho:
                    velocidade_x=0
                    velocidade_y=tamanho
        ##preenche tela com uma cor    
        fundo.fill(azul)
        ##cria objeto no meio da tela
        pos_x+=velocidade_x
        pos_y+=velocidade_y

        
        cobracabeca = []
        ##colocando dentro da lista o valor da pos_x e pos_y
        cobracabeca.append(pos_x)
        cobracabeca.append(pos_y)
        ##colocando cobracabeca dentro da lista cobraxy
        cobraxy.append(cobracabeca)
        ##se cobra for maior cobracomp deletar cobra na posicao 0 para ela nao ficar infinita
        if len(cobraxy) > cobracomp:
            del cobraxy[0]
        ## se qualquer um dos blocos for igual a cobracabeca para cada bloco da cobraxy vamos fazer que seja gameover
        if any(blocos == cobracabeca for blocos in cobraxy[:-1]):
            pass
        
        ##lista cobraxy
        cobra(cobraxy)
        ##quando comer a maca, ela muda de posição
        if pos_x == maca_x and pos_y == maca_y:
            maca_x = randint(0,(largura-tamanho)/10)*10
            maca_y = randint(0,(altura-tamanho)/10)*10
            ##ao passar sobre a maca a cobra cresce um pixel
            cobracomp += 1

        maca(maca_x, maca_y)
        
        pygame.display.update()
        ##quantidade de frames por segundo
        relogio.tick(15)
        if pos_x > largura:
            pos_x = 0
        if pos_x < 0:
            pos_x = largura-tamanho
        if pos_y > altura:
            pos_y = 0
        if pos_y < 0:
            pos_y = altura-tamanho
    ##bloquear de passar pela parede
    ##    if pos_x > largura:
    ##        sair = False
    ##    if pos_x < 0:
    ##        sair = False
    ##    if pos_y > altura:
    ##        sair = False
    ##    if pos_y < 0:
    ##        sair = False
jogo()                
pygame.quit()

