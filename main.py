import pygame 
import sys

import bird
import tube
import ai

class Game :
    def __init__(self, control) :
        # game parameter
        self.WIDTH = 288
        self.HEIGHT= 512
        self.score = 0
        self.player_control = control
        self.count = 1450

        # bird parameter
        self.bird = bird.Bird(self.WIDTH, self.HEIGHT)

        # tube parameter
        self.tube = tube.TubeList(self.WIDTH, self.HEIGHT)

        # ai parameter
        self.q_learning = ai.AI()

        pygame.init()
        self.screen = pygame.display.set_mode((self.WIDTH, self.HEIGHT))

    def game_loop (self) :
        self.reset()
        jump = False
        pass_tube = False
        while True:
            pygame.time.delay(1)
            if self.count > 100000000 :
                self.count = 0
            else :
                self.count = self.count + 1
            jump = False
            for event in pygame.event.get():
                if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and  
                    event.key == pygame.K_ESCAPE):
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE :
                    jump = True

            if self.player_control is True :
                jump = self.q_learning.get_action(self.bird, self.tube.tube_list, self.score)

            # clean screen
            self.screen.fill((0, 0, 0))

            # bird
            self.bird.update_and_draw(self.screen, jump)

            print(self.count)
            #tube
            (end, in_tube) = self.tube.update(self.bird, self.screen, self.count%1510==0)
            self.q_learning.request_reward(jump, end, self.bird, self.tube.tube_list)

            if end :
                self.reset()
                pass_tube = False

            if in_tube and (not pass_tube) :
                pass_tube = True
            elif not in_tube and pass_tube :
                self.score = self.score + 1
                pass_tube = False
            else :
                pass
            
            # draw
            #self.screen.blit(self.screen, (0,0))
            pygame.display.flip()
            #pygame.display.update

        self.q_learning.store_date()

    def reset(self) :
        self.bird.reset()
        self.tube.reset()
        self.count = 1450
        self.score = 0


def main () :
    if len(sys.argv) == 1 :
        print("[INFO] User control mode")
        game = Game(False)
        game.game_loop()
    elif len(sys.argv) == 2 :
        print("[INFO] AI control mode")
        game = Game(True)
        game.game_loop()
    else :
        print("Please use [program] ai")
        sys.exit()



if __name__ == '__main__' :
    main()
