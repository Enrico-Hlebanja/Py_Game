# ===== Inicialização =====
# ----- Importa e inicia pacotes
import pygame
import random

pygame.init()

# ----- Gera tela principal
window = pygame.display.set_mode((600, 700))
HEIGHT = 700
pygame.display.set_caption('SUPER JOGO DO ENRICO')
brick_image = pygame.image.load('assets/img/Fundo.png').convert()
brick_image = pygame.transform.scale(brick_image, (600, 700))
janela_image = pygame.image.load('assets/img/Janela.png').convert()
janela_image = pygame.transform.scale(janela_image, (100, 150))
janelaA_image1 = pygame.image.load('assets/img/JanelaA1.png').convert()
janelaA_image1 = pygame.transform.scale(janelaA_image1, (100, 150))
janelaA_image2 = pygame.image.load('assets/img/JanelaA2.png').convert()
janelaA_image2 = pygame.transform.scale(janelaA_image2, (100, 150))
janelaA_image3 = pygame.image.load('assets/img/JanelaA3.png').convert()
janelaA_image3 = pygame.transform.scale(janelaA_image3, (100, 150))
janelaA_image4 = pygame.image.load('assets/img/JanelaA4.png').convert()
janelaA_image4 = pygame.transform.scale(janelaA_image4, (100, 150))
janelaA_image5 = pygame.image.load('assets/img/JanelaA5.png').convert()
janelaA_image5 = pygame.transform.scale(janelaA_image5, (100, 150))
score_font = pygame.font.Font('assets/font/PressStart2P.ttf', 50)

Imagens = [janelaA_image2]

# ----- Inicia estruturas de dados
game = True
janela1=[[1,1],[1,2],[2,1],[2,2],[1,3],[2,3]]
janela2=[[5,1],[5,2],[5,3],[6,1],[6,2],[6,3]]
janela3=[[9,1],[9,2],[9,3],[10,1],[10,2],[10,3]]
janela4=[[1,5],[1,6],[1,7],[2,5],[2,6],[2,7]]
janela5=[[5,5],[5,6],[5,7],[6,5],[6,6],[6,7]]
janela6=[[9,5],[9,6],[9,7],[10,5],[10,6],[10,7]]
janela7=[[1,9],[1,10],[1,11],[2,9],[2,10],[2,11]]
janela8=[[5,9],[5,10],[5,11],[6,9],[6,10],[6,11]]
janela9=[[9,9],[9,10],[9,11],[10,9],[10,10],[10,11]]
intervalo = [250,500,750,100,1000]
ABERTA=[False,False,False,False,False,False,False,False,False]
Velocidade = 2000
Coordenadas =[[50,50],[250,50],[450,50],[50,250],[250,250],[450,250],[50,450],[250,450],[450,450]]
areaj= [[1,1],[1,2],[2,1],[2,2],[1,3],[2,3],[5,1],[5,2],[5,3],[6,1],[6,2],[6,3],[9,1],[9,2],[9,3],[10,1],[10,2],[10,3],[1,5],[1,6],[1,7],[2,5],[2,6],[2,7],[5,5],[5,6],[5,7],[6,5],[6,6],[6,7],[9,5],[9,6],[9,7],[10,5],[10,6],[10,7],[1,9],[1,10],[1,11],[2,9],[2,10],[2,11],[5,9],[5,10],[5,11],[6,9],[6,10],[6,11],[9,9],[9,10],[9,11],[10,9],[10,10],[10,11]]
Tempo = pygame.time.get_ticks()
Tempo2 = 0
c = 0
lives = 3
# ===== Loop principal =====
while game:


    
    if ABERTA[0] and ABERTA[1] and ABERTA[2] or  ABERTA[3] and ABERTA[4] and ABERTA[5] or  ABERTA[6] and ABERTA[7] and ABERTA[8]:
        game = False
    if ABERTA[0] and ABERTA[3] and ABERTA[6] or  ABERTA[1] and ABERTA[4] and ABERTA[7] or  ABERTA[2] and ABERTA[5] and ABERTA[8]:
        game = False
    if ABERTA[0] and ABERTA[4] and ABERTA[8] or  ABERTA[2] and ABERTA[4] and ABERTA[6]:
        game = False
    # ----- Trata eventos
    Janelas=[0]*9
    for event in pygame.event.get():
        # ----- Verifica consequências
        if event.type == pygame.QUIT:
            game = False
        if lives == 0:
            game = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            pos = pygame.mouse.get_pos()
            
            if [pos[0]//50,pos[1]//50] in janela1:
                Janelas[0]=1
            if [pos[0]//50,pos[1]//50] in janela2:
                Janelas[1]=2
            if [pos[0]//50,pos[1]//50] in janela3:
                Janelas[2]=3
            if [pos[0]//50,pos[1]//50] in janela4:
                Janelas[3]=4
            if [pos[0]//50,pos[1]//50] in janela5:
                Janelas[4]=5
            if [pos[0]//50,pos[1]//50] in janela6:
                Janelas[5]=6
            if [pos[0]//50,pos[1]//50] in janela7:
                Janelas[6]=7
            if [pos[0]//50,pos[1]//50] in janela8:
                Janelas[7]=8
            if [pos[0]//50,pos[1]//50] in janela9:
                Janelas[8]=9

#---------------- Verifica se o click foi valido

            if[pos[0]//50,pos[1]//50]  not in areaj:
                lives-=1
            for e in Janelas:
                if e > 0 and ABERTA[e-1] == False:
                    lives-=1
                if e > 0 and ABERTA[e-1] == True:
                    ABERTA[e-1] = False

# ------------- Imgens e Configurações
    window.blit(brick_image,(0,0))
    
    i=-1
    for e in ABERTA:
        i+=1
        if e == False:
            window.blit(janela_image,(Coordenadas[i]))

    #------------- velocidade-----------------
    agora2=pygame.time.get_ticks()
    if agora2 - Tempo2 == 5000:
        if Velocidade>200:
            Tempo2 = agora2
            Velocidade -= 100

        
    

    #-------------Abre janelas
    agora=pygame.time.get_ticks()
    if agora - Tempo > Velocidade: 
        Tempo = agora
        n = random.randint(0,8)
        for e in range(8):
            if e == n:
                print(Velocidade)
                ABERTA[n]=True
                b=random.randint(0,0)
    #-------------Verifica se a janela está aberta
    if ABERTA[0]==True:
        
        window.blit(Imagens[b],(Coordenadas[0]))
    if ABERTA[1]==True:
        
        window.blit(Imagens[b],(Coordenadas[1]))
    if ABERTA[2]==True:
        
        window.blit(Imagens[b],(Coordenadas[2]))
    if ABERTA[3]==True:
        
        window.blit(Imagens[b],(Coordenadas[3]))
    if ABERTA[4]==True:
        
        window.blit(Imagens[b],(Coordenadas[4]))
    if ABERTA[5]==True:
        
        window.blit(Imagens[b],(Coordenadas[5]))
    if ABERTA[6]==True:
        
        window.blit(Imagens[b],(Coordenadas[6]))
    if ABERTA[7]==True:
        
        window.blit(Imagens[b],(Coordenadas[7]))
    if ABERTA[8]==True:
        
        window.blit(Imagens[b],(Coordenadas[8]))
    
        
    # ----- Atualiza estado do jogo
    text_surface = score_font.render(chr(9829) * lives, True, (100, 100, 200))
    text_rect = text_surface.get_rect()
    text_rect.bottomleft = (10, HEIGHT - 10)
    window.blit(text_surface, text_rect)
    

    pygame.display.update()  # Mostra o novo frame para o jogador
# ===== Finalização =====
pygame.quit()  # Função do PyGame que finaliza os recursos utilizados
