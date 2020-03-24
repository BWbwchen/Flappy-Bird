import pygame 
import random
import time


class Tube:
    def __init__ (self, WIDTH, HEIGHT) :
        random.seed(time.time())
        self.tube_width = 40 
        self.tube_gap = random.randrange(101, 300)
        self.tube_height = random.randrange(10, 200)
        self.HEIGHT = HEIGHT
        self.tube_x = WIDTH 
        self.tube_velocity = 0.1
        self.tube_touch = False

    def update_and_draw (self, screen):
        self.__draw_tubes(screen) 
        self.__update_tubes() 

    def __draw_tubes (self, screen) :
        white = (255, 255, 255)
        red = (255, 0, 0)
        color = white
        # top tube

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


class TubeList :
    def __init__ (self, WIDTH, HEIGHT) :
        self.SCREEN_WIDTH = WIDTH
        self.SCREEN_HEIGHT = HEIGHT
        self.tube_list = []
        self.t = 0

    def update (self, bird, screen, flag) :
        self.t = self.t + 1
        (end, in_tube) = self.__detect_collision(bird)
        self.__deal_tube_list(screen, flag)
        if self.t == 2500:
            #print("delta is :" + str(int(self.tube_list[1].tube_x - self.tube_list[0].tube_x)))
            #print(self.tube_list)
            self.t = 0
        return (end, in_tube)

    def __deal_tube_list (self, screen, flag) :
        if flag :
            self.tube_list.append(Tube(self.SCREEN_WIDTH, self.SCREEN_HEIGHT))

        for i, val in enumerate(self.tube_list): 
            val.update_and_draw(screen)
            val.tube_touch = False
            if val.tube_x < 0 :
                self.tube_list.pop(i)

    def __detect_collision(self, bird) :
        in_tube = False
        for i, val in enumerate(self.tube_list):
            if ((val.tube_x <= bird.x <= val.tube_x + val.tube_width) or\
                (val.tube_x <= bird.x+bird.size <= val.tube_x+val.tube_width)) and\
                ((bird.y <= val.tube_height) or\
                (bird.y+bird.size >= val.tube_height+val.tube_gap)) :
                self.reset()
                #print("gameover")
                #print("score is : " + str(self.score))
                val.tube_touch = True
                return (True, in_tube)
            elif bird.y >= self.SCREEN_HEIGHT - 5:
                val.tube_touch = True
                return (True, in_tube)
            elif (val.tube_x <= bird.x <= val.tube_x + val.tube_width) :
                in_tube = True
                # PASS the tube
                # TODO : slow down the add
                #print("pass")
                #print("score is : " + str(self.score))
                # TODO : score
                #self.score += self.increase
        self.bird_x_pre = bird.x
        return (False, in_tube)

    def reset(self):
        self.tube_list = []
