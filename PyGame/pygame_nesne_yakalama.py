import pygame,sys
import time,numpy

pygame.init()

class Game:
    def __init__(self):
        self.window_width = 1200
        self.window_height = 720
        self.window = pygame.display.set_mode((self.window_width,self.window_height))
        pygame.display.set_caption("Cath Me Baby")
        self.clock = pygame.time.Clock()
        
        self.arkaplan= pygame.transform.scale(pygame.image.load("Pygame/Füzeden kaçış/arkaplan.jpg"),(self.window_width,self.window_height))
        self.missile= pygame.transform.scale(pygame.image.load("Pygame/Füzeden kaçış/missile.png"),(150,25))
        self.leftrun= pygame.transform.scale(pygame.image.load("Pygame/Füzeden kaçış/Playerleft.png"),(150,150))
        self.rightrun= pygame.transform.scale(pygame.image.load("Pygame/Füzeden kaçış/Playerright.png"),(150,150))
        self.bumbum= pygame.transform.scale(pygame.image.load("Pygame/Füzeden kaçış/patlama.png"),(180,180))
        self.Player= pygame.transform.scale(pygame.image.load("Pygame/Füzeden kaçış/Player.png"),(150,150))
        self.Heart= pygame.transform.scale(pygame.image.load("Pygame/Füzeden kaçış/Heart.png"),(50,50))
        self.nextLevel= pygame.transform.scale(pygame.image.load("Pygame/Füzeden kaçış/nextLevel.png"),(500,300))
        self.gameOver= pygame.transform.scale(pygame.image.load("Pygame/Füzeden kaçış/Game over.png"),(800,500))
        self.PlayerLose= pygame.transform.scale(pygame.image.load("Pygame/Füzeden kaçış/PlayerLose.png"),(150,150))
        self.PlayerWin= pygame.transform.scale(pygame.image.load("Pygame/Füzeden kaçış/Win.png"),(380,380))


        self.PlayerX,self.PlayerY  = 500,420
        self.missileX,self.missileY=[None,None,None,None,None],[None,None,None,None,None]
        self.oldtime = int(time.time())
        self.boom = [None,None,None,None,None]
        self.bombX,self.bombY = [None,None,None,None,None],[None,None,None,None,None]
        self.winner=0
        self.Life = 3
        self.fast=0
        
    def draw(self):#oyun bilgilerini bastırır
        self.window.blit(self.arkaplan,(0,0))
        self.key = pygame.key.get_pressed()

        if self.Life == -1:
            self.window.blit(self.gameOver,(180,100))
            self.window.blit(self.PlayerLose, (self.PlayerX, self.PlayerY))

        elif self.Life>-1 and self.fast==8:
            self.window.blit(self.PlayerWin,(380,30))
            self.window.blit(self.Player, (self.PlayerX, self.PlayerY))

        elif self.Life>-1 and self.winner>20:
            self.window.blit(self.nextLevel,(330,100))
            self.window.blit(self.Player, (self.PlayerX, self.PlayerY))
            self.fast+=2
            self.winner=0

        else:
            if self.key[pygame.K_d]:
                self.window.blit(self.rightrun, (self.PlayerX, self.PlayerY))
            elif self.key[pygame.K_a]:
                self.window.blit(self.leftrun, (self.PlayerX, self.PlayerY))
            else:
                self.window.blit(self.Player, (self.PlayerX, self.PlayerY))
        
        for x in range(5):
            if self.missileX[x] is not None:
                self.window.blit(self.missile,(self.missileX[x],self.missileY[x]))
        
        for x in range(5):
            if self.boom[x] is not None and time.time()-self.boom[x]<0.1:
                if self.bombX[x] is not None:
                    self.window.blit(self.bumbum,(self.bombX[x],self.bombY[x]))
        
        for x in range(self.Life):
            self.window.blit(self.Heart,(x*self.Heart.get_size()[0],0))




        self.clock.tick(60)
        pygame.display.update()

    def game_loop(self):#oyun bilgilerini günceller
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

        self.key = pygame.key.get_pressed()
        if self.key[pygame.K_ESCAPE]:
            return 0

        if self.Life>-1 and self.winner<=20 and self.fast<8:
            if self.key[pygame.K_d]:
                if self.PlayerX+self.Player.get_size()[0]<1200:
                    self.PlayerX += 8
            elif self.key[pygame.K_a]:
                if self.PlayerX>0:
                    self.PlayerX -= 8


            if int(time.time()) == self.oldtime+1:
                for x in range(5):
                    if self.missileX[x] is None:
                        self.missileX[x] = numpy.random.randint(0,1200-self.missile.get_size()[0])
                        self.missileY[x] = 50
                        self.oldtime = int(time.time())
                        break
            
            for x in range(5):
                if self.missileX[x] is not None:
                    self.missileY[x] += 4+self.fast
                    if self.missileY[x]+self.missile.get_size()[1]>600:
                        self.boom[x] = time.time()
                        self.bombX[x] = self.missileX[x]
                        self.bombY[x] = 450
                        self.winner +=1
                        self.missileX[x]=None
                        self.missileY[x]=None
                        

            for x in range(5):
                if self.missileX[x] is not None:
                    if self.PlayerX>self.missileX[x] and self.PlayerX < self.missileX[x]+self.missile.get_size()[0]:
                        if self.missileY[x]>self.PlayerY and self.missileY[x]<self.PlayerY+self.Player.get_size()[1]:
                            self.Life-=1
                            self.boom[x] = time.time()
                            self.bombX[x] = self.missileX[x]
                            self.bombY[x] = self.missileY[x]-80
                            self.missileX[x]=None
                            self.missileY[x]=None

                        elif self.missileY[x]+self.missile.get_size()[1]>self.PlayerY and self.missileY[x]+self.missile.get_size()[1]<self.PlayerY+self.Player.get_size()[1]:
                            self.Life-=1
                            self.boom[x] = time.time()
                            self.bombX[x] = self.missileX[x]
                            self.bombY[x] = self.missileY[x]-80
                            self.missileX[x]=None
                            self.missileY[x]=None

                    elif self.PlayerX+self.Player.get_size()[0]>self.missileX[x] and self.PlayerX+self.Player.get_size()[0] < self.missileX[x]+self.missile.get_size()[0]:
                        if self.missileY[x]>self.PlayerY and self.missileY[x]<self.PlayerY+self.Player.get_size()[1]:
                            self.Life-=1
                            self.boom[x] = time.time()
                            self.bombX[x] = self.missileX[x]
                            self.bombY[x] = self.missileY[x]-80
                            self.missileX[x]=None
                            self.missileY[x]=None

                        elif self.missileY[x]+self.missile.get_size()[1]>self.PlayerY and self.missileY[x]+self.missile.get_size()[1]<self.PlayerY+self.Player.get_size()[1]:
                            self.Life-=1
                            self.boom[x] = time.time()
                            self.bombX[x] = self.missileX[x]
                            self.bombY[x] = self.missileY[x]-80
                            self.missileX[x]=None
                            self.missileY[x]=None

        self.draw()

def fuzeden_kac():#oynu başlatır
    game = Game()

    while True:
        game_status = game.game_loop()
        if game_status is not None:
            break

    pygame.quit()