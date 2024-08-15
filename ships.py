import pygame
class Ship:
    def __init__(self,ai_game):
        self.screen=ai_game.screen
        self.screen_rect = ai_game.screen.get_rect()
        self.settings = ai_game.settings

        #加载飞船的图像

        self.image = pygame.image.load("images/meme.png")
        self.rect = self.image.get_rect()

        #设置位置
        self.rect.midbottom = self.screen_rect.midbottom
       
        self.x = float(self.rect.x)
        #新增移动标志位
        self.moving_right = False
        self.moving_left = False
        #self.moving_up = False
        #self.moving_down = False
       

        
        



    def update(self):
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.x += self.settings.ship_speed
        if self.moving_left and self.rect.left  > 0:
            self.x -= self.settings.ship_speed
        
        self.rect.x = self.x
      
        
    def blitme(self):
        #绘制飞船
       self.screen.blit(self.image,self.rect)


    def center_ship(self):
        self.rect.midbottom = self.screen_rect.midbottom
        self.x = float(self.rect.x)