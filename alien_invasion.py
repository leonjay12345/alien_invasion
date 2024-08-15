import sys 

from time import sleep
 
import pygame

from settings import Settings

from ships import Ship

from bullets import Bullet

from alien import Alien

from game_stats import GameStats

from button import Button

class AlienInvasion:
    def __init__(self):
        pygame.init()
        self.clock = pygame.time.Clock()
        self.settings = Settings()

        #游戏启动后处于活动状态
        self.active = False
        #创建按钮
        #self.play_button = Button(self,"Play")



        self.screen = pygame.display.set_mode((self.settings.screen_width,self.settings.screen_height))
        pygame.display.set_caption("Alien Invasion")
        #创建一个用于存储游戏统计信息的实例
        self.stats = GameStats(self)
        



        #创建类的实例
        self.ship = Ship(self)
        self.bullets = pygame.sprite.Group()
        self.bg_color = self.settings.bg_color

        self.aliens = pygame.sprite.Group()
        self._create_fleet()
        #创建按钮
        self.play_button = Button(self,"Play")


    def _create_alien(self,x_position,y_position):
         new_alien = Alien(self)
         new_alien.x = x_position
         
         new_alien.rect.x = new_alien.x
         new_alien.y = y_position
         new_alien.rect.y = new_alien.y

         self.aliens.add(new_alien)
         

    def _create_fleet(self):
        alien = Alien(self)

        #alien_width = alien.rect.width
        alien_width,alien_height = alien.rect.size
        #current_x = alien_width
        current_x,current_y = alien_width,alien_height
           
        while current_y < (self.settings.screen_height - 3*alien_height):
            while current_x < (self.settings.screen_width - 2*alien_width):
                 self._create_alien(current_x,current_y)
                 current_x +=2*alien_width
            current_x = alien_width
            current_y+=2*alien_height


        
        alien = Alien(self)
        self.aliens.add(alien)






    def _check_keydown_events(self,event):
        if event.key == pygame.K_RIGHT:
             self.ship.moving_right = True
        elif event.key == pygame.K_LEFT:
             self.ship.moving_left = True
        
        elif event.key == pygame.K_q:
             sys.exit()
        elif event.key == pygame.K_SPACE:
                    #self._fire_bullet()
             self._fire_bullet()
             file = r"menwai_02.mp3"
             pygame.mixer.init()
             track = pygame.mixer.music.load(file)
             pygame.mixer.music.play()

             


    def _check_keyup_events(self,event):
        if event.key == pygame.K_RIGHT:    
                    self.ship.moving_right = False
        elif event.key == pygame.K_LEFT:
                    self.ship.moving_left = False 
        



    def _check_events(self): 
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                self._check_keydown_events(event)
                #if event.key == pygame.K_UP:
                    #self.ship.moving_up = True
                #if event.key == pygame.K_DOWN:
                    #self.ship.moving_down = True
            elif event.type == pygame.KEYUP:
                self._check_keyup_events(event)
                
                #if event.key == pygame.K_UP:
                    #self.ship.moving_up = False
                #if event.key ==pygame.K_DOWN:
                    #self.ship.moving_down = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                 mouse_pos = pygame.mouse.get_pos()
                 self._check_play_button(mouse_pos)               
    def _check_play_button(self,mouse_pos):
         button_clicked = self.play_button.rect.collidepoint(mouse_pos)
         if button_clicked and not self.active:
              self.stats.reset_stats()

              self.active  = True
              #清空列表
              self.bullets.empty()
              self.aliens.empty()
              #将创建的新的飞船放置在屏幕底部中央
              self.ship.center_ship()



    def _update_screen(self):
        
        self.screen.fill(self.settings.bg_color)
        self.ship.blitme()
        for bullet in self.bullets.sprites():
              bullet.draw_bullet()
       
        self.ship.blitme()
        self.aliens.draw(self.screen)
        if  not self.active:
             self.play_button.draw_button()

                
    

        pygame.display.flip()
              
              


    def _fire_bullet(self):
        new_bullet = Bullet(self)
        #self.bullets.add(new_bullet)
        
         
        self.bullets.add(new_bullet)
    def _check_bullet_alien_collision(self):
         #检查是否有子弹击中外星人
        collisions = pygame.sprite.groupcollide(self.bullets,self.aliens,False,True)
        if not self.aliens:
             self.bullets.empty()
             self._create_fleet()
         
    
    
    
    
    
    def _update_bullets(self):
        self._check_bullet_alien_collision()

        self.bullets.update()
        for bullet in self.bullets.copy():
                if bullet.rect.bottom  <= 0:
                      self.bullets.remove(bullet)



    def _change_fleet_direction(self):
         #让整个舰队向下移动，同事修改左右移动的方向
         for alien in self.aliens.sprites():
              alien.rect.y += self.settings.fleet_drop_speed
         self.settings.fleet_direction *= -1
            
              


    def _check_fleet_edges(self):
         for alien in self.aliens.sprites():
              if alien.check_edges():
                   self._change_fleet_direction()
                   break      
              

    def _ship_hit(self):
        if self.stats.ship_left > 0:
            self.stats.ship_left -=1
            print(f"ship_left:{self.stats.ship_left}")
            #清空外星人列表和子弹列表
            self.aliens.empty()
            self.bullets.empty()
            #将飞船放在屏幕的底部中央
            self.ship.center_ship()
            #stop for a minute
            sleep(0.5)
        else:
             self.active = False
        



        





    def _update_aliens(self):
         #检查是否有外星人到达边缘
         self._check_fleet_edges()
         self.aliens.update()
         #检测外星人和飞船是否发生碰撞
         if pygame.sprite.spritecollideany(self.ship,self.aliens):
              print("Ship hit aliens")
              self._ship_hit()
        #检测是否有外星人到达下边缘
         self._check_aliens_bottom()

    def _check_aliens_bottom(self):
         for alien in self.aliens.sprites():
              if alien.rect.bottom >= self.settings.screen_height:
                   #想像飞船撞到外星人一样处理
                   self._ship_hit()
                   break
    

    
    def run_game(self):
        while True:
          self._check_events()
          if self.active:

            self.ship.update()
            #self.bullets.update()
                        #刷新屏幕
            self._update_screen()
            self._update_bullets()
            self._update_aliens()
            
                

        
            
          pygame.display.flip() 
          self._update_screen()
          self.clock.tick(60) 


if __name__ == "__main__":
    ai = AlienInvasion()
    ai.run_game()


     


        