import pygame
from pygame.sprite import  Sprite
\

class Alien(Sprite):
    def __init__(self, ai_game):
        super().__init__()
        self.screen = ai_game.screen
        self.settings = ai_game.settings


        #load pictures,set info
        self.image = pygame.image.load("alien_invasion/images/laoda.png")
        self.rect = self.image.get_rect()
       
       #set the begining position for aliens
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height
    #   store the position
        self.x = float(self.rect.x)

    def check_edges(self):
        screen_rect = self.screen.get_rect()#获取屏幕
        return (self.rect.right >= screen_rect.right)  or (self.rect.left <= 0)

        


    def update(self):
        #向右移动alien
        self.x +=self.settings.alien_speed * self.settings.fleet_direction
        self.rect.x = self.x
