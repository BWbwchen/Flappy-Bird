import pygame 
import sys

import bird
import tube

class Game :
    def __init__(self) :
        # game parameter
        self.WIDTH = 288
        self.HEIGHT= 512
        self.score = 0
        self.increase = 1

        # bird parameter
        self.bird = bird.Bird(self.WIDTH, self.HEIGHT)

        # tube parameter
        self.tube = tube.TubeList(self.WIDTH, self.HEIGHT)

        pygame.init()
        self.screen = pygame.display.set_mode((self.WIDTH, self.HEIGHT))

    def game_loop (self) :
        self.reset()
        jump = False
        count = -1
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
            self.bird.update_and_draw(self.screen, jump)

            #tube
            self.tube.update(self.bird, self.screen, count%2000==0)
            
            # draw
            self.screen.blit(self.screen, (0,0))
            pygame.display.flip()
            #pygame.display.update

    def reset(self) :
        self.bird.reset()
        self.tube.reset()




game = Game()
game.game_loop()
