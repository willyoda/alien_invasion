import sys 
import pygame
from settings import Settings
from ship import Ship
from pygame.constants import K_RIGHT, QUIT

class AlienInvasion:
    """管理游戏资源和行为的类"""

    def __init__(self):
        """初始化游戏资源并创建游戏资源"""
        pygame.init()
       
        pygame.display.set_caption("Alien Invasion")
        # self.screen = pygame.display.set_mode((1200,800))
        # self.bg_color = (230,230,230)
        # self.screen.fill(self.bg_color)

        self.settings = Settings()    
        self.screen = pygame.display.set_mode((self.settings.screen_width,self.settings.screen_height))
        # self.screen.fill(self.settings.bg_color)

        self.ship = Ship(self)

    def run_game(self):
        while True:
            self._check_events()
            # self.ship.update()
            # self.ship.blitme()
            # pygame.display.flip()

            self._update_screen()

    def _update_screen(self):
        self.screen.fill(self.settings.bg_color)
        self.ship.update()
        self.ship.blitme()
        pygame.display.flip()

    def _check_events(self):
        """响应按键和鼠标"""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            # ****** 这部分代码可以实现  右移  start ****
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RIGHT:
                    # self.ship.rect.x +=1
                    self.ship.moving_right = True
                if event.key == pygame.K_LEFT:
                    self.ship.moving_left = True
                if event.key == pygame.K_UP:
                    self.ship.moving_up = True
                if event.key == pygame.K_DOWN:
                    self.ship.moving_down = True

            elif event.type == pygame.KEYUP:
                if event.key == pygame.K_RIGHT:
                    self.ship.moving_right = False  
                if event.key == pygame.K_LEFT:
                    self.ship.moving_left = False  
                if event.key == pygame.K_UP:
                    self.ship.moving_up = False  
                if event.key == pygame.K_DOWN:
                    self.ship.moving_down = False  

            # ****** 这部分代码可以实现  右移  end****




if __name__ == '__main__':
    ai= AlienInvasion()
    ai.run_game()
