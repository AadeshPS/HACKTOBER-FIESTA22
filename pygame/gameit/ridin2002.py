import pygame
import random
import math

def webshooters():
    pygame.init()


    screen=pygame.display.set_mode((800,600))




    pygame.display.set_caption("web shooters ")
    icon=pygame.image.load('spider.png')
    pygame.display.set_icon(icon)


    playerImg=pygame.image.load('spider.png')
    playerX=370
    playerY=480
    playerX_change =0



    enemyImg=[]
    enemyX=[]
    enemyY=[]
    enemyX_change =[]
    enemyY_change =[]
    num_of_enemies=6

    for i in range(num_of_enemies):
        enemyImg.append(pygame.image.load('bug.png'))
        enemyX.append(random.randint(0,735))
        enemyY.append(random.randint(50,150))
        enemyX_change.append(0.3)
        enemyY_change.append(40)




    bulletImg=pygame.image.load('web.png')
    bulletX= 0
    bulletY=480
    bulletX_change =0
    bulletY_change =.3
    global bullet_state
    bullet_state="ready"


    score_value=0
    font=pygame.font.Font('freesansbold.ttf',32)

    textX=10
    testY=10


    over_font=pygame.font.Font('freesansbold.ttf',64)

    def show_score(x,y):
        score=font.render("score:"+str(score_value),True,(0,0,0))
        screen.blit(score,(x,y))

    def game_over_text():
        over_text=over_font.render("GAME OVER",True,(0,0,0))
        screen.blit(over_text,(200,250))

    def player(x,y):
        screen.blit(playerImg,(x,y))

    def enemy(x,y,i):
        screen.blit(enemyImg[i],(x,y))

    def fire_bullet(x,y):
        global bullet_state
        bullet_state="fire"
        screen.blit(bulletImg,(x+16,y+10))

    def iscollision(enemyX,enemyY,bulletX,bulletY):
        distance= math.sqrt((math.pow(enemyX-bulletX,2)+math.pow(enemyY-bulletY,2)))   
        if distance <27:
            return True
        else:
            return False
    running=True
    while running:
    
        screen.fill((255,255,255))
        
        
        for event in pygame.event.get():
                if event.type==pygame.QUIT:
                    running=False

            
                if event.type==pygame.KEYDOWN:
                    if event.key==pygame.K_LEFT:
                        playerX_change =-0.3
                    if event.key==pygame.K_RIGHT:
                        playerX_change =0.3


                    
                    if event.key==pygame.K_UP:
                        if bullet_state is "ready":
                            bulletX=playerX
                            fire_bullet(playerX,bulletY)

                    
                if event.type==pygame.KEYUP:
                    if event.key==pygame.K_LEFT or event.key==pygame.K_RIGHT:
                        playerX_change=0

                
        playerX+=playerX_change

        if playerX<=0:
            playerX =0
        elif playerX >= 736:
            playerX =736
            
        
        for i in range(num_of_enemies):
            
            if enemyY[i]>450:
                for j in range(num_of_enemies):
                    enemyY[j]=2000
                game_over_text()
                break

            
            enemyX[i]+=enemyX_change[i]

            if enemyX[i]<=0:
                enemyX_change[i]=0.3
                enemyY[i]+=enemyY_change[i]
            elif enemyX[i] >= 736:
                enemyX_change[i] =-0.3
                enemyY[i]+=enemyY_change[i]

            
            collision=iscollision(enemyX[i],enemyY[i],bulletX,bulletY)
            if collision:
                bulletY=480
                bullet_state="ready"
                score_value+=1
                print(score_value)
                enemyX[i]= random.randint(0,735)
                enemyY[i]=random.randint(50,150)
            enemy(enemyX[i],enemyY[i],i)


        if bulletY<=0:
            bulletY=480
            bullet_state="ready"
        if bullet_state is "fire":
            fire_bullet(bulletX,bulletY)
            bulletY -=bulletY_change

            
            
        player(playerX,playerY)
        show_score(textX,testY)


        pygame.display.update()
