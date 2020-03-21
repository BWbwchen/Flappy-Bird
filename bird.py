import pygame 
class Bird :
    def __init__ (self, WIDTH, HEIGHT) :
        self.WIDTH = WIDTH
        self.HEIGHT= HEIGHT
        self.x = self.WIDTH/4
        self.y = self.HEIGHT/2
        self.size = 20
        self.gravity = 0.0007
        self.lift = 0.4
        self.velocity = 0
    def update_and_draw (self, screen, jump) :
        self.__draw_bird(screen)
        self.__update_bird(jump)
    def reset (self):
        self.x = self.WIDTH/4
        self.y = self.HEIGHT/2
        self.velocity = 0
    def __draw_bird(self, screen) :
        pygame.draw.circle(screen, (255, 255, 255), 
                (int(self.x), int(self.y)), self.size//2)
    def __update_bird(self, jump) :
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
