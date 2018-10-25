##importando biblioteca pygame
import pygame
##biblioteca que pega um numero de um intervalo de numeros
from random import randrange

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
largura = 320
altura = 280
##define tamanho do objeto que desenhamos
tamanho = 10
placar = 40
##relogio que define fps
relogio = pygame.time.Clock()
##fundo do jogo com altura e largura
fundo = pygame.display.set_mode((largura,altura))
##nome que fica no topo da janela do jogo
pygame.display.set_caption("Jogo Snake")


def texto(msg, cor,tam,x,y):
    font = pygame.font.SysFont(None,tam)
    texto1 = font.render(msg, True,cor)
    fundo.blit(texto1, [x,y])

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
    fimdejogo = False
    pos_x = randrange(0,largura-tamanho,10)
    pos_y = randrange(0,altura-tamanho-placar,10)
    maca_x = randrange(0,largura-tamanho,10)
    maca_y = randrange(0,altura-tamanho-placar,10)
    velocidade_x=0
    velocidade_y=0
    cobraxy = []
    cobracomp = 1
    pontos = 0
    while sair:
        while fimdejogo:
            fundo.fill(branco)
            texto('Game Over, [C] Continuar [S] Sair', vermelho, 20, largura/10, altura/2)
            pygame.display.update()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sair = False
                    fimdejogo = False
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_c:
                        sair = True
                        fimdejogo = False
                        pos_x = randrange(0,largura-tamanho,10)
                        pos_y = randrange(0,altura-tamanho-placar,10)
                        maca_x = randrange(0,largura-tamanho,10)
                        maca_y = randrange(0,altura-tamanho-placar,10)
                        velocidade_x=0
                        velocidade_y=0
                        cobraxy = []
                        cobracomp = 1
                        pontos = 0
                    if event.key == pygame.K_s:
                        sair = False
                        fimdejogo = False
        for event in pygame.event.get():
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
        if sair:
            ##preenche tela com uma cor    
            fundo.fill(branco)
            ##cria objeto no meio da tela
            pos_x+=velocidade_x
            pos_y+=velocidade_y

            ##quando comer a maca, ela muda de posição
            if pos_x == maca_x and pos_y == maca_y:
                maca_x = randrange(0,largura-tamanho,10)
                maca_y = randrange(0,altura-tamanho-placar,10)
                ##ao passar sobre a maca a cobra cresce um pixel
                cobracomp += 1
                ##ganha + 1 ponto ao comer maça
                pontos += 1

            if pos_x + tamanho > largura:
                fimdejogo = True
            if pos_x < 0:
                fimdejogo = True
            if pos_y + tamanho > altura - placar:
                fimdejogo = True
            if pos_y < 0:
                fimdejogo = True
            ##if pos_x > largura:
            ##  pos_x = 0
            ##if pos_x < 0:
            ##  pos_x = largura-tamanho
            ##if pos_y > altura:
            ##  pos_y = 0
            ##if pos_y < 0:
            ##  pos_y = altura-tamanho
                
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
                fimdejogo = True
            

            pygame.draw.rect(fundo, preto, [0, altura-placar, largura, placar])
            texto("Pontuação:"+str(pontos),branco,20,10,altura-30)
            ##lista cobraxy
            cobra(cobraxy)     
            maca(maca_x, maca_y)
            pygame.display.update()
            ##quantidade de frames por segundo
            relogio.tick(15)
            ##game over ao bater na parede
            
jogo()                
pygame.quit()

