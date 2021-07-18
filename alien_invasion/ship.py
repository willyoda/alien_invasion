import pygame
class Ship:
    """ship class"""
    def __init__(self,ai_name):
        """init class"""
        self.screen =ai_name.screen
        self.screen_rect = ai_name.screen.get_rect()
        # 加载飞船图像并获取其外形矩形

        # self.image = pygame.image.load('D:/Python/alien_invasion/images/ship.bmp') #方法1绝对路径ok
        # self.image = pygame.image.load('./images/ship.bmp') #方法相对路径
        self.image = pygame.image.load('./images/ship.png') #方法相对路径
        
        self.rect = self.image.get_rect()
        # self.rect.midbottom = self.screen_rect.midbottom
        self.rect.bottomleft = self.screen_rect.bottomleft

        self.moving_right = False
        self.moving_left = False
        self.moving_up = False
        self.moving_down = False
    def update(self):
        if self.moving_right:
            # if self.rect.x <= self.screen.get_width():
               self.rect.x +=1    
        if self.moving_left:
            # if self.rect.x > 0:
                self.rect.x -=1
        if self.moving_up:
                self.rect.y -=1
        if self.moving_down:
                self.rect.y +=1

    def blitme(self):
         self.screen.blit(self.image,self.rect)