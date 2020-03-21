import pygame 
import sys
# for random tube gap
import random
import time

class Game :
    def __init__(self) :
        # game parameter
        self.WIDTH = 288
        self.HEIGHT= 512
        self.score = 0
        self.increase = 1

        # bird parameter
        self.x = self.WIDTH/4
        self.y = self.HEIGHT/2
        self.size = 20
        self.gravity = 0.0007
        self.lift = 0.4
        self.velocity = 0

        # tube parameter
        self.tube = self.Tube(self.WIDTH, self.HEIGHT)
        self.tube_list = []

        pygame.init()
        self.screen = pygame.display.set_mode((self.WIDTH, self.HEIGHT))

    def game_loop (self) :
        self.reset()
        jump = False
        self.tube_list.append(self.Tube(self.WIDTH, self.HEIGHT))
        count = 0
        while True:
            if count > 100000000 :
                count = 0
            else :
                count = count + 1
            jump = False
            for event in pygame.event.get():
                if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and  
                    event.key == pygame.K_ESCAPE):
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE :
                    jump = True

            # clean screen
            self.screen.fill((0, 0, 0))

            # bird
            self.draw_bird()
            self.update_bird(jump)

            #tube
            self.detect_collision()
            self.deal_tube_list(count%2000==0)
            
            # draw
            self.screen.blit(self.screen, (0,0))
            pygame.display.flip()
            #pygame.display.update

    def reset(self) :
        self.x = self.WIDTH/4
        self.y = self.HEIGHT/2
        self.velocity = 0
        self.score = 0

        self.tube = self.Tube(self.WIDTH, self.HEIGHT)
        self.tube_list = []


    def draw_bird (self) :
        pygame.draw.circle(self.screen, (255, 255, 255), 
                (int(self.x), int(self.y)), self.size//2)

    def update_bird (self, jump) :
        if jump :
            # TODO : if press space many time the velocity will be very small
            self.velocity -= self.lift
        else :
            self.velocity += self.gravity

        self.y += self.velocity

        if self.y > self.HEIGHT:
            self.y = self.HEIGHT
            self.velocity = 0
        elif self.y < 0 :
            self.y = 0 
            self.velocity = 0

    def deal_tube_list (self, flag) :
        if flag :
            self.tube_list.append(self.Tube(self.WIDTH, self.HEIGHT))

        for i, val in enumerate(self.tube_list): 
            val.update_and_draw(self.screen)
            val.tube_touch = False
            if val.tube_x < 0 :
                self.tube_list.pop(i)
        
    
    def detect_collision(self) :
        for i, val in enumerate(self.tube_list):
            if ((val.tube_x <= self.x <= val.tube_x + val.tube_width) or\
                (val.tube_x <= self.x+self.size <= val.tube_x+val.tube_width)) and\
                ((self.y <= val.tube_height) or\
                (self.y+self.size >= val.tube_height+val.tube_gap)) :
                #self.reset()
                print("gameover")
                print("score is : " + str(self.score))
                val.tube_touch = True
            elif (val.tube_x <= self.x <= val.tube_x + val.tube_width) or\
                (val.tube_x <= self.x+self.size <= val.tube_x+val.tube_width):
                # TODO : slow down the add
                print("pass")
                print("score is : " + str(self.score))
                self.score += self.increase

    # ---------------- inner class ---------------#
    class Tube:
        def __init__ (self, WIDTH, HEIGHT) :
            random.seed(time.time())
            self.tube_width = 40 
            self.tube_gap = random.randrange(100, 300)
            self.tube_height = random.randrange(10, 200)
            self.HEIGHT = HEIGHT
            self.tube_x = WIDTH 
            self.tube_velocity = 0.1
            self.tube_touch = False

        def update_and_draw (self, screen):
            self.__draw_tubes(screen) 
            self.__update_tubes() 

        def __draw_tubes (self, screen) :
            # top tube
            white = (255, 255, 255)
            red = (255, 0, 0)
            color = white

            if self.tube_touch :
                color = red

            pygame.draw.rect(screen, color, 
                    (self.tube_x, 0, self.tube_width, self.tube_height), 0)
            # buttom tube
            pygame.draw.rect(screen, color, 
                    (self.tube_x, self.tube_height + self.tube_gap, 
                     self.tube_width, 
                         self.HEIGHT - self.tube_height - self.tube_gap), 0)

        def __update_tubes (self) :
            self.tube_x -= self.tube_velocity


game = Game()
game.game_loop()
