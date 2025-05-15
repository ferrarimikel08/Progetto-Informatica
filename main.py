import pygame,sys
from pygame.locals import *
pygame.init()

BLACK = (0,0,0)
WHITE = (255,255,255)
RED = (255,0,0)

window_width = 900
window_height = 600
window_size = (window_width,window_height)
screen = pygame.display.set_mode(window_size)
pygame.display.set_caption("Labirinto")

clock = pygame.time.Clock()
fps = 60

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.display.quit()
            pygame.quit()
            sys.exit()
    pygame.display.flip()