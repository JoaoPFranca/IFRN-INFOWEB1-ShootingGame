import pygame
import math
import random
pygame.init()
pygame.font.init()
pygame.mixer.init()

# Importando imagens
menu = pygame.image.load('menuKK.png')
background = pygame.image.load('novobackground.png')
arma1 = pygame.image.load('armap1.png')
arma2 = pygame.image.load('armap2.png')
balaft = pygame.image.load('bala.png')
balap1 = pygame.image.load('balap1.png')
balap2 = pygame.image.load('balap2.png')
icone = pygame.image.load('iconjogo.png')

#Criando Tela
TELA = pygame.display.set_mode((1024, 720))

#Título e Ícone
pygame.display.set_caption("Shooting Game")
pygame.display.set_icon(icone)

#Game Over
Fonte = pygame.font.Font('Mario-Kart-DS.ttf', 80)
FonteK = pygame.font.Font('Mario-Kart-DS.ttf', 40)



def gameovertxt():
    fimtxt = Fonte.render("DOMINADO", True, (255,255,255))
    TELA.blit(fimtxt, (300, 300))

def pressk():
    fimtxt = FonteK.render("Aperte K para sair", True, (255,255,255))
    TELA.blit(fimtxt, (335, 450))


#pontuacao
ndepontos = 0
font = pygame.font.Font('Mario-Kart-DS.ttf', 42)
textox = 10
textoy = 10

def Placar(x,y):
    placar = font.render((" NUMERO DE KILLS -     ") + str(ndepontos), True, (255,0,255))
    TELA.blit(placar, (x, y))

# Player 1
player1x = 0
player1y = 100
vel1 = 0


def player1(x, y):
    TELA.blit(arma1, (x, y))

# Player 2
player2x = 0
player2y = 450
vel2 = 0

def player2(x, y):
    TELA.blit(arma2, (x, y))

# Inimigo
inimigoft = []
inimigox = []
inimigoy = []
velinimigox = []
velinimigoy = []
ndeinimigos = 20

for i in range(ndeinimigos):
 inimigoft.append(pygame.image.load('naveeee.png'))
 inimigox.append(random.randint(850, 900))
 inimigoy.append(random.randint(5, 600))
 velinimigox.append(100)
 velinimigoy.append(1)

def inimigo(x, y, i):
    TELA.blit(inimigoft[i], (x, y))

# Bala
balax = 0
balay = 100
balavelx = 10
balavely = 0
pente1carregado = "pronta"


# Bala2
bala2x = 0
bala2y = 450
bala2velx = 10

pente2carregado = "pronta"


def bala1(x, y):
    global pente1carregado
    pente1carregado = "tiro"
    TELA.blit(balap1, (x, y - 31))

def bala2(x, y):
    global pente2carregado
    pente2carregado = "tiro"
    TELA.blit(balap2, (x , y - 31))

def colisao1(inimigox, inimigoy, balax, balay):
    distancia1 = math.sqrt((math.pow(inimigox - balax,2)) + (+ math.pow(inimigoy - balay,2)))
    if distancia1 < 27:
        return True
    else:
        return False

def colisao2(inimigox, inimigoy, bala2x, bala2y):
    distancia2 = math.sqrt((math.pow(inimigox - bala2x,2)) + (+ math.pow(inimigoy - bala2y,2)))
    if distancia2 < 27:
        return True
    else:
        return False


#Loop

#estado = menu
#TELA.blit(menu, (0, 0))

running2 = True
while running2:
    TELA.blit(menu, (0, 0))
    pygame.display.update()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_k:
                running2 = False

running = True
while running:


    pygame.mixer.music.stop()

    TELA.blit(background, (0, 0))


    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False


        #Movimentação das armas
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_w:
                vel1 = -1
            if event.key == pygame.K_s:
                vel1 = 1
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_w or event.key == pygame.K_s:
                vel1 = 0
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                vel2 = -1
            if event.key == pygame.K_DOWN:
                vel2 = 1
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                vel2 = 0


        #Atirar da bala
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_d:
                if pente1carregado == "pronta":
                 balay = player1y
                 bala1(player1y, balay)
                 tirobala = pygame.mixer.Sound('tiro_jogo.wav')
                 tirobala.play()

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                if pente2carregado == "pronta":
                 bala2y = player2y
                 bala2(player2y, bala2y)
                 tirobala = pygame.mixer.Sound('tiro_jogo.wav')
                 tirobala.play()


    player1y += vel1
    player2y += vel2

    #Bordas pros Players
    if player1y <= -50:
        player1y = -50
    elif player1y >= 600:
        player1y = 600
    if player2y <= -50:
        player2y = -50
    elif player2y >= 600:
        player2y = 600

    # Movimento dos inimigos
    for i in range(ndeinimigos):
     if inimigox[i] < 0:
            for j in range(ndeinimigos):
                inimigoy[i] = -2000
            gmover = pygame.mixer.Sound('gameover_jogo.wav')
            gmover.play()
            gameovertxt()
            textox = 5000   # fazendo sumir da tela
            player1x = 5000 # fazendo sumir da tela
            player2x = 5000 # fazendo sumir da tela
            balax = 5000
            bala2x = 5000
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_k:
                        running = False
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.QUIT:
                        running = False
            pressk()


     inimigoy[i] += velinimigoy[i]
     # Bordas pros inimigos
     if inimigoy[i] <= -100:
        velinimigoy[i] = 2
        inimigox[i] -= velinimigox[i]
     elif inimigoy[i] >= 700:
        velinimigoy[i] = -2
        inimigox[i] -= velinimigox[i]

     # COLISÃO
     primeiracolisao = colisao1(inimigox[i], inimigoy[i], balax, balay)
     if primeiracolisao:
         balax = 1025
         pente1carregado = "pronto"
         ndepontos += 1
         inimigox[i] = random.randint(850, 900)
         inimigoy[i] = random.randint(5, 600)
         colisaosom = pygame.mixer.Sound('explosao4.mp3')
         colisaosom.play()

     segundacolisao = colisao2(inimigox[i], inimigoy[i], bala2x, bala2y)
     if segundacolisao:
         bala2x = 1025
         pente2carregado = "pronto"
         ndepontos += 1
         inimigox[i] = random.randint(850, 900)
         inimigoy[i]= random.randint(5, 600)
         colisaosom = pygame.mixer.Sound('explosao4.mp3')
         colisaosom.play()

     inimigo(inimigox[i], inimigoy[i], i)


    # Movimento da bala
    if balax >= 1024:
        balax = 0
        pente1carregado = "pronta"
    if bala2x >= 1024:
        bala2x = 0
        pente2carregado = "pronta"


    if pente1carregado == "tiro":
        bala1(balax, balay)
        balax += balavelx
    if pente2carregado == "tiro":
        bala2(bala2x, bala2y)
        bala2x += bala2velx

    player1(player1x, player1y)
    player2(player2x, player2y)
    Placar(textox, textoy)
    pygame.display.update()

