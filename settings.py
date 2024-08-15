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
        self.alien_speed = 10
        self.fleet_direction = 1
        self.fleet_drop_speed = 5
        #1代表向右，-1代表向左

