import time
import random
import pygame
pygame.init()
class player:
    snakes=[7,4,35,22,60,40,70,34,74,54,84,90,99,24]
    ladders=[5,16,9,13,21,23,28,53,42,46,56,85,62,78,69,73,94,96]
    plpos=[(150,515),(200,515),(250,515),(300,515),(350,515),(400,515),(450,515),(500,515),(550,515),(600,515),(600,465),(550,465),(500,465),(450,465),(400,465),(350,465),(300,465),(250,465),(200,465),(150,465),(150,415),(200,415),(250,415),(300,415),(350,415),(400,415),(450,415),(500,415),(550,415),(600,415),(600,365),(550,365),(500,365),(450,365),(400,365),(350,365),(300,365),(250,365),(200,365),(150,365),(150,315),(200,315),(250,315),(300,315),(350,315),(400,315),(450,315),(500,315),(550,315),(600,315),(600,265),(550,265),(500,265),(450,265),(400,265),(350,265),(300,265),(250,265),(200,265),(150,265),(150,215),(200,215),(250,215),(300,215),(350,215),(400,215),(450,215),(500,215),(550,215),(600,215),(600,165),(550,165),(500,165),(450,165),(400,165),(350,165),(300,165),(250,165),(200,165),(150,165),(150,115),(200,115),(250,115),(300,115),(350,115),(400,115),(450,115),(500,115),(550,115),(600,115),(600,65),(550,65),(500,65),(450,65),(400,65),(350,65),(300,65),(250,65),(200,65),(150,65)]
    player_pos=0
    def __init__(self, pl):
        self.player=pl
    def checkpos(self):
        for i in range(0,len(self.ladders),2):
            if(self.player_pos==self.ladders[i]):
                print("Yay! ",self.player," got a ladder")
                self.player_pos=self.ladders[i+1]
        for i in range(0,len(self.snakes),2): 
            if(self.player_pos==self.snakes[i]):
                print("Opps! ",self.player," got caught by a snake")
                self.player_pos=self.snakes[i+1]

def text(msg,color,dispx,dispy,font):
    screen_text=font.render(msg,True,color)
    screen.blit(screen_text,[dispx,dispy])

def gamedtls():
    pygame.draw.rect(screen,black, [675,19,300,525], 2)
    pygame.draw.rect(screen,gray, [700,25,150, 100])
    pawn(blue,(786,37))
    pawn(red,(786,87))
    text("Player 1: ",black,700,25,pygame.font.SysFont('Times New Roman',20)) 
    text("Player 2: ",black,700,75,pygame.font.SysFont('Times New Roman',20)) 

def die(pl):
    dice=["C:\\Users\\gokul.DESKTOP-PJOSIK2\\Documents\\Pygame\\Snakes n ladder\\1.png","C:\\Users\\gokul.DESKTOP-PJOSIK2\\Documents\\Pygame\\Snakes n ladder\\2.png","C:\\Users\\gokul.DESKTOP-PJOSIK2\\Documents\\Pygame\\Snakes n ladder\\3.png","C:\\Users\\gokul.DESKTOP-PJOSIK2\\Documents\\Pygame\\Snakes n ladder\\4.png","C:\\Users\\gokul.DESKTOP-PJOSIK2\\Documents\\Pygame\\Snakes n ladder\\5.png","C:\\Users\\gokul.DESKTOP-PJOSIK2\\Documents\\Pygame\\Snakes n ladder\\6.png"]
    for i in range(0,6):
        screen.blit(pygame.image.load(dice[i]),(750,300))
        pygame.display.update()
        time.sleep(0.25)
    if(pl==1):
        screen.blit(pygame.image.load(dice[0]),(750,300))
        pygame.display.update()
    elif(pl==2):
        screen.blit(pygame.image.load(dice[1]),(750,300))
        pygame.display.update()
    elif(pl==3):
        screen.blit(pygame.image.load(dice[2]),(750,300))
        pygame.display.update()
    elif(pl==4):
        screen.blit(pygame.image.load(dice[3]),(750,300))
        pygame.display.update()
    elif(pl==5):
        screen.blit(pygame.image.load(dice[4]),(750,300))
        pygame.display.update()
    elif(pl==6):
        screen.blit(pygame.image.load(dice[5]),(750,300))
        pygame.display.update()

def pawn(color,n1):
    pygame.draw.circle(screen,color,n1,15)
    pygame.draw.circle(screen,white,n1,5)

def main():
    screen.blit(board,(120,30))
    player1=player("Player 1")
    player2=player("Player 2")
    ch=1
    player2.player_pos=1
    gamedtls()
    time.sleep(2)
    while(player1.player_pos!=100 and player2.player_pos!=100):
        pl1=random.randint(1,6)
        print("Player 1: ",pl1)
        pygame.draw.rect(screen,gray, [700, 150, 150, 100])
        text("Player 1: "+str(pl1),black,700,150,pygame.font.SysFont('Times New Roman',25))
        die(pl1)
        pygame.display.update()
        if(player1.player_pos+pl1>100):
            player1.player_pos+=0
        else:
            for i in range(pl1):
                player1.player_pos+=1
                screen.blit(board,(120,30))
                pawn(red,player2.plpos[player2.player_pos-1])
                pawn(blue,player1.plpos[player1.player_pos-1])
                pygame.display.update()
                time.sleep(0.5)
        if(player1.player_pos==100):
            print("Congrats ",player1.player," won!")
            screen.fill(gray)
            text("Player 1 has won!",black,200,200,pygame.font.SysFont('Times New Roman',40))  
            pygame.display.update()
            time.sleep(2)
            break
        player1.checkpos()
        screen.blit(board,(120,30))
        gamedtls()
        pawn(red,player2.plpos[player2.player_pos-1])
        pawn(blue,player1.plpos[player1.player_pos-1])
        pygame.display.update()
        print("You are at: ",player1.player_pos)
        print("---------------------------------------------------")
        time.sleep(2)
        if (ch==1):
            player2.player_pos=0
            ch=2
        pl2=random.randint(1,6)
        print("Player 2: ",pl2)
        pygame.draw.rect(screen,gray, [700, 150, 150, 100])
        text("Player 2: "+str(pl2),black,700,150,pygame.font.SysFont('Times New Roman',25))
        pygame.display.update()
        die(pl2)
        if(player2.player_pos+pl2>100):
            player2.player_pos+=0
        else: 
            for i in range(pl2):
                player2.player_pos+=1
                screen.blit(board,(120,30))
                pawn(blue,player1.plpos[player1.player_pos-1])
                pawn(red,player2.plpos[player2.player_pos-1])
                pygame.display.update()
                time.sleep(0.5)
        if(player2.player_pos==100):
            print("Congrats ",player2.player," won!")
            screen.fill(gray)
            text("Player 2 has won!",black,200,200,pygame.font.SysFont('Times New Roman',40))  
            pygame.display.update()
            time.sleep(2)
            break
        player2.checkpos()
        screen.blit(board,(120,30))
        pawn(blue,player1.plpos[player1.player_pos-1])
        pawn(red,player2.plpos[player2.player_pos-1])
        pygame.display.update()
        print("You are at: ",player2.player_pos)
        print("---------------------------------------------------")
        time.sleep(2)
pygame.display.set_caption("SnakesnLadders")
gray=(217,217,217)
black=(0,0,0)
white=(255,255,255)
blue=(0,96,255)
red=(255,0,0)
dispx=1000
dispy=1000
screen = pygame.display.set_mode((dispx,dispy))
screen.fill(gray)
board=pygame.image.load("C:\\Users\\gokul.DESKTOP-PJOSIK2\\Documents\\Pygame\\Snakes n ladder\\snakesnladder.PNG")
main()