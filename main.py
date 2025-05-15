import pygame,sys
from pygame.locals import *
from maze import Maze
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

cell_size = 10

maze = Maze("gamemap1.txt")

maze_width, maze_height = maze.get_matrix_size()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.display.quit()
            pygame.quit()
            sys.exit()
    maze.draw_maze(screen,maze_height,maze_width,cell_size,RED,WHITE)

    pygame.display.update()
    pygame.display.flip()
    clock.tick(60)