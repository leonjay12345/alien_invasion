import pygame


class Settings:

    def __init__(self):
        self.screen_width = 800
        self.screen_height = 600
        self.bg_color = (250,200,255)
        
        self.ship_speed = 10
        self.ship_limit = 3
        

        

        #bullets settings
        self.bullet_speed = 6.0
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = (0,0,0) 
        #alien settings
        self.alien_speed = 3
        self.fleet_direction = 1
        self.fleet_drop_speed = 4
        #1代表向右，-1代表向左
        self.score_scale = 1.5

        #用什么速度来增加难度
        self.speed_scale = 1.1
        self.initialize_dynamic_settings()
    def initialize_dynamic_settings(self):
        self.alien_speed = 1.0
        #积分设置
        self.alien_score = 1000

    def increase_speed(self):
        self.alien_speed*=self.speed_scale
        self.ship_speed*=self.speed_scale
        self.alien_score=int(self.alien_score*self.score_scale)
        print(self.alien_score)




