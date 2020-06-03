import pygame
import Pygame_theColors
import random 
import time

pygame.init()

gameDisplay=pygame.display.set_mode((600,630)) #() for tuple

pygame.display.set_caption("Tic-Tac-Toe")

white=(255,255,255)#r,g,b
black=(0,0,0)
red=(255,0,0)
green=(0,255,0)
blue=(0,0,255)
aquamarine2=(118,238,198)

mousex=0
mousey=0

box1=True
box2=True
box3=True
box4=True
box5=True
box6=True
box7=True
box8=True
box9=True

turncount=0
turnDisplay="Square's Turn"

gameDisplay.fill(white)

def textComicSansMS(msg,x,y,color=white, size=10):
    font=pygame.font.SysFont('Comic Sans MS', size)
    m=font.render(msg, True, color)
    gameDisplay.blit(m,(x,y))
    

def textAriel(msg,x,y,color=white, size=10):
    font=pygame.font.SysFont('Ariel', size)
    m=font.render(msg, True, color)
    gameDisplay.blit(m,(x,y))

def board():
    rectx1=0
    recty1=0
    red=(255,0,0)
    green=(0,255,0)
    white=(255,255,255)
    black=(0,0,0)
    for x in range(0,3,1):
        for y in range(0,3,1):
            pygame.draw.rect(gameDisplay, black, (rectx1,recty1,200,200))
            recty1+=200
            (black,white)=(white,black)
        recty1=0
        rectx1+=200
        
def circle(xcenter,ycenter):
    pygame.draw.circle(gameDisplay, blue, (xcenter+100,ycenter+100), 90,20)

def square(squarex, squarey):
    pygame.draw.rect(gameDisplay, blue, (squarex+20,squarey+20,160,160), 20)


threewin={1:'',2:'',3:'',4:'',5:'',6:'',7:'',8:'',9:''}


sgameOver=False
cgameOver=False
gameOver=False
tiegameOver=False

board()
pygame.display.update()
while True:

    pygame.display.update()#under while loop
    
    for event in pygame.event.get():#loop through events

        if event.type==pygame.QUIT: #event are caps
            pygame.quit()#X out of pygame
            quit()#exit()#quit out of shell
##        if event.type == pygame.MOUSEMOTION:
##            print("mouse at :",event.pos)
##            (mousexd,mouseyd)=event.pos
##            textAriel((mousexd,mouseyd),10,610,black,10)
        #Left Mouse button = 1 Middle = 2 Right = 3
        elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            print( "You pressed the left mouse button at",event.pos)
            (mousex,mousey)=event.pos
##            turncount=turncount+1
        elif event.type == pygame.MOUSEBUTTONUP and event.button == 1:
            print ("You released the left mouse button at",event.pos)

        elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 2:
            print( "You pressed the middle mouse button at",event.pos)
        elif event.type == pygame.MOUSEBUTTONUP and event.button == 2:
            print ("You released the middle mouse button at",event.pos)

        elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 3:
            print( "You pressed the right mouse button at",event.pos)
        elif event.type == pygame.MOUSEBUTTONUP and event.button == 3:
            print ("You released the right mouse button at",event.pos)

                
        #if event.type==pygame.KEYDOWN:
        #elif event.type==pygame.KEYUP:
    if turncount%2==1 and gameOver==False:
        turnDisplay="Circle's Turn"
        if 0<mousex<200 and 0<mousey<200 and box1==True:
            circle(0,0)
            threewin[1]='c'
            box1=False
            turncount=turncount+1
        if 200<mousex<400 and 0<mousey<200 and box2==True:
            circle(200,0)
            box2=False
            turncount=turncount+1
            threewin[2]='c'
        if 400<mousex<600 and 0<mousey<200 and box3==True:
            circle(400,0)
            box3=False
            turncount=turncount+1
            threewin[3]='c'
        if 0<mousex<200 and 200<mousey<400 and box4==True:
            circle(0,200)
            box4=False
            turncount=turncount+1
            threewin[4]='c'
        if 200<mousex<400 and 200<mousey<400 and box5==True:
            circle(200,200)
            box5=False
            turncount=turncount+1
            threewin[5]='c'
        if 400<mousex<600 and 200<mousey<400 and box6==True:
            circle(400,200)
            box6=False
            turncount=turncount+1
            threewin[6]='c'
        if 0<mousex<200 and 400<mousey<600 and box7==True:
            circle(0,400)
            box7=False
            turncount=turncount+1
            threewin[7]='c'
        if 200<mousex<400 and 400<mousey<600 and box8==True:
            circle(200,400)
            box8=False
            turncount=turncount+1
            threewin[8]='c'
        if 400<mousex<600 and 400<mousey<600 and box9==True:
            circle(400,400)
            box9=False
            turncount=turncount+1
            threewin[9]='c'
    elif turncount%2==0 and gameOver==False:
        turnDisplay="Square's Turn"
        if 0<mousex<200 and 0<mousey<200 and box1==True:
            square(0,0)
            box1=False
            turncount=turncount+1
            threewin[1]='s'
        if 200<mousex<400 and 0<mousey<200 and box2==True:
            square(200,0)
            box2=False
            turncount=turncount+1
            threewin[2]='s'
        if 400<mousex<600 and 0<mousey<200 and box3==True:
            square(400,0)
            box3=False
            turncount=turncount+1
            threewin[3]='s'
        if 0<mousex<200 and 200<mousey<400 and box4==True:
            square(0,200)
            box4=False
            turncount=turncount+1
            threewin[4]='s'
        if 200<mousex<400 and 200<mousey<400 and box5==True:
            square(200,200)
            box5=False
            turncount=turncount+1
            threewin[5]='s'
        if 400<mousex<600 and 200<mousey<400 and box6==True:
            square(400,200)
            box6=False
            turncount=turncount+1
            threewin[6]='s'
        if 0<mousex<200 and 400<mousey<600 and box7==True:
            square(0,400)
            box7=False
            turncount=turncount+1
            threewin[7]='s'
        if 200<mousex<400 and 400<mousey<600 and box8==True:
            square(200,400)
            box8=False
            turncount=turncount+1
            threewin[8]='s'
        if 400<mousex<600 and 400<mousey<600 and box9==True:
            square(400,400)
            threewin[9]='s'
            box9=False
            turncount=turncount+1


    if threewin[1]==threewin[2]==threewin[3]=='s':
        pygame.draw.line(gameDisplay, red, (100,100), (500,100),30)
        sgameOver=True
    elif threewin[4]==threewin[5]==threewin[6]=='s':
        pygame.draw.line(gameDisplay, red, (100,300), (500,300),30)
        sgameOver=True
    elif threewin[7]==threewin[8]==threewin[9]=='s':
        pygame.draw.line(gameDisplay, red, (100,500), (500,500),30)
        sgameOver=True
    elif threewin[1]==threewin[4]==threewin[7]=='s':
        pygame.draw.line(gameDisplay, red, (100,100), (100,500),30)
        sgameOver=True
    elif threewin[2]==threewin[5]==threewin[8]=='s':
        pygame.draw.line(gameDisplay, red, (300,100), (300,500),30)
        sgameOver=True
    elif threewin[3]==threewin[6]==threewin[9]=='s':
        pygame.draw.line(gameDisplay, red, (500,100), (500,500),30)
        sgameOver=True
    elif threewin[1]==threewin[5]==threewin[9]=='s':
        pygame.draw.line(gameDisplay, red, (100,100), (500,500),30)
        sgameOver=True
    elif threewin[3]==threewin[5]==threewin[7]=='s':
        pygame.draw.line(gameDisplay, red, (500,100), (100,500),30)
        sgameOver=True

    elif threewin[1]==threewin[2]==threewin[3]=='c':
        pygame.draw.line(gameDisplay, red, (100,100), (500,100),30)
        cgameOver=True
    elif threewin[4]==threewin[5]==threewin[6]=='c':
        pygame.draw.line(gameDisplay, red, (100,300), (500,300),30)
        cgameOver=True
    elif threewin[7]==threewin[8]==threewin[9]=='c':
        pygame.draw.line(gameDisplay, red, (100,500), (500,500),30)
        cgameOver=True
    elif threewin[1]==threewin[4]==threewin[7]=='c':
        pygame.draw.line(gameDisplay, red, (100,100), (100,500),30)
        cgameOver=True
    elif threewin[2]==threewin[5]==threewin[8]=='c':
        pygame.draw.line(gameDisplay, red, (300,100), (300,500),30)
        cgameOver=True
    elif threewin[3]==threewin[6]==threewin[9]=='c':
        pygame.draw.line(gameDisplay, red, (500,100), (500,500),30)
        cgameOver=True
    elif threewin[1]==threewin[5]==threewin[9]=='c':
        pygame.draw.line(gameDisplay, red, (100,100), (500,500),30)
        cgameOver=True
    elif threewin[3]==threewin[5]==threewin[7]=='c':
        pygame.draw.line(gameDisplay, red, (500,100), (100,500),30)
        cgameOver=True

    elif threewin[1]!='' and threewin[2]!='' and threewin[3]!='' and threewin[4]!='' and threewin[5]!='' and threewin[6]!='' and threewin[7]!='' and threewin[8]!='' and threewin[9]!='' and cgameOver==False and sgameOver==False:  
        tiegameOver=True


    if gameOver==False:
        pygame.draw.rect(gameDisplay, white, (10,605,100,100))
        textAriel(turnDisplay,10,610,black,20)
    if sgameOver==True:
        gameOver=True
        threewin[1]=''
        threewin[2]=''
        threewin[3]=''
        threewin[4]=''
        threewin[5]=''
        threewin[6]=''
        threewin[7]=''
        threewin[8]=''
        threewin[9]=''
        print('\nSquare Wins!\n')
##        textAriel('Square Wins!', 510,610,black,20)
        pygame.draw.rect(gameDisplay, white, (10,605,100,100))
        textAriel('Square Wins!',10,610,black,20)
        sgameOver=False
        
    if cgameOver==True:
        gameOver=True
        threewin[1]=''
        threewin[2]=''
        threewin[3]=''
        threewin[4]=''
        threewin[5]=''
        threewin[6]=''
        threewin[7]=''
        threewin[8]=''
        threewin[9]=''
        print('\nCircle Wins!\n')
##        textAriel('Cicle Wins!', 520,610,black,20)
        pygame.draw.rect(gameDisplay, white, (10,605,100,100))
        textAriel('Cicle Wins!',10,610,black,20)
        cgameOver=False

    if tiegameOver==True:
        gameOver=True
        threewin[1]=''
        threewin[2]=''
        threewin[3]=''
        threewin[4]=''
        threewin[5]=''
        threewin[6]=''
        threewin[7]=''
        threewin[8]=''
        threewin[9]=''
        print('\nTie!\n')
##        textAriel('Tie!', 540,610,black,20)
        pygame.draw.rect(gameDisplay, white, (10,605,100,100))
        textAriel('Tie!',10,610,black,20)        
        tiegameOver=False
    
##           
##    pygame.draw.rect(gameDisplay, white, (10,605,100,100))
##    textAriel(turnDisplay,10,610,black,20)
##    
    
    textAriel('Tic-Tac-Toe',510,610,black,20)
    pygame.draw.line(gameDisplay, black, (0,600),(600,600))    
    
