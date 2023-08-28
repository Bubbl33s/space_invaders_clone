import pygame

from aliens_arrays import *


class Alien:
    def __init__(self, window, x, y, frame_1, frame_2):
        self.window = window
        self.x = x
        self.y = y
        self.size = 36
        self.block_size = self.size / 12
        self.speed = 0.01
        self.last_animation_time = pygame.time.get_ticks()
        self.animation_state = 0
        
        self.frame_1 = frame_1
        self.frame_2 = frame_2
        
     
    def draw(self):
        current_time = pygame.time.get_ticks()
        
        if current_time - self.last_animation_time > 1000:
            # Alternamos entre los dos frames
            self.animation_state = 1 - self.animation_state  # Esta línea alterna entre 0 y 1
            self.last_animation_time = current_time

        # Usamos el frame de animación basado en el estado
        actual_frame = self.frame_1 if self.animation_state == 0 else self.frame_2
            
        for row, row_val in enumerate(actual_frame):
            for col, col_val in enumerate(row_val):
                if col_val:
                    pygame.draw.rect(self.window.screen, "#FFFFFF", 
                                    pygame.Rect(self.x + col*self.block_size, self.y + row*self.block_size,
                                                self.block_size, self.block_size))
        self.y += self.speed


class Generator:
    def __init__(self, window):
        self.window = window
        self.margin = 30
        self.pad = 50
        
        self.width_range = range(self.margin, self.window.width - self.margin, self.pad)
        self.height_range = range(self.margin, self.pad*5, self.pad)
        
        self.frames_list = [(alien_1a, alien_1b), (alien_2a, alien_2b), (alien_2a, alien_2b),
                            (alien_3a, alien_3b), (alien_3a, alien_3b)]
        
        for x in self.width_range:
            for y, frames in zip(self.height_range, self.frames_list):
                self.window.aliens.append(Alien(self.window, x, y, frames[0], frames[1]))
