import time
import random
class player:
    snakes=[11,3,14,10,19,8]
    ladders=[2,6,5,12,9,17]
    player_pos=0
    def __init__(self, pl):
        self.player=pl
    def checkpos(self):
        for i in range(0,len(self.snakes),2):
            if(self.player_pos==self.ladders[i]):
                print("Yay! ",self.player," got a ladder")
                self.player_pos=self.ladders[i+1]
            elif(self.player_pos==self.snakes[i]):
                print("Opps! ",self.player," got caught by a snake")
                self.player_pos=self.snakes[i+1]

def main():
    player1=player("Player 1")
    player2=player("Player 2")
    time.sleep(2)
    while(player1.player_pos!=20 and player2.player_pos!=20):
        pl1=random.randint(1,6)
        print("Player 1: ",pl1)
        player1.player_pos+=pl1
        if(player1.player_pos>20):
            player1.player_pos-=pl1
        if(player1.player_pos==20):
            print("Congrats ",player1.player," won!");
            break
        player1.checkpos()
        print("You are at: ",player1.player_pos)
        print("---------------------------------------------------")
        time.sleep(2)
        pl2=random.randint(1,6)
        print("Player 2: ",pl2)
        player2.player_pos+=pl2
        if(player2.player_pos>20):
            player2.player_pos-=pl2
        if(player2.player_pos==20):
            print("Congrats ",player2.player," won!");
            break
        player2.checkpos()
        print("You are at: ",player2.player_pos)
        print("---------------------------------------------------")
        time.sleep(2)
main()