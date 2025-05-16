import pygame,sys
from pygame.locals import *
from maze import Maze
from player import Player
pygame.init()

BLACK = (0,0,0)
WHITE = (255,255,255)
RED = (255,0,0)
BLUE = (0,0,255)

window_width = 1200
window_height = 600
window_size = (window_width,window_height)
pygame.display.set_caption("Labirinto")

clock = pygame.time.Clock()
fps = 30

cell_size = 50
levels = ["gamemap5.txt","gamemap1.txt"]

for level in levels:
    maze = Maze(level)
    player = Player(level)
    screen = pygame.display.set_mode(window_size)

    maze_width, maze_height = maze.get_matrix_size()
    play = True

    while play:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.display.quit()
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN and player.is_win==False:            
                if event.key==pygame.K_LEFT:
                    player.move_left()
                elif event.key==pygame.K_RIGHT:
                    player.move_right()
                elif event.key==pygame.K_UP:
                    player.move_up()
                elif event.key==pygame.K_DOWN:
                    player.move_down()
            elif event.type == pygame.KEYDOWN and player.is_win==True:
                if event.key == pygame.K_RETURN:
                    play = False
        
    

        maze.draw_maze(screen,maze_height,maze_width,cell_size)
        player.draw_player(screen,cell_size)
        if player.is_win:
            player.draw_win(screen,window_width/2,window_height/2)
        pygame.display.update()
        pygame.display.flip()
        clock.tick(fps)

    