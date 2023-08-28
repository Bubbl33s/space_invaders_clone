import pygame
from alien import *


class Window:
    def __init__(self, width, height, fps):
        pygame.init()
        self.aliens = []
        self.width = width
        self.height = height
        self.screen = pygame.display.set_mode((self.width, self.height))
        pygame.display.set_caption("Space Invaders")
        self.clock = pygame.time.Clock()
        self.fps = fps
        self.done = False
        pygame.mouse.set_visible(False)
        
        generator = Generator(self)
    
    def run_game(self):
        while not self.done:
            self.clock.tick(self.fps)
            self.event_handler()
            
            self.screen.fill("#000000")
            
            for alien in self.aliens:
                alien.draw()
            
            pygame.display.flip()     
    
    def event_handler(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.done = True
