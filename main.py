import pygame,sys
from pygame.locals import *
from maze import Maze
from player import Player
pygame.init()

window_width = 1200
window_height = 600
window_size = (window_width,window_height)
window_color = (120,30,35)
pygame.display.set_caption("Labirinto")

clock = pygame.time.Clock()
fps = 30

cell_size = 50
levels = ["gamemap1.txt", "gamemap2.txt", "gamemap3.txt", "gamemap4.txt", "gamemap5.txt"]
times = []
level_number = len(levels)
for level in levels:
    current_time = 0
    start_time = pygame.time.get_ticks()
    level_number = level_number-1
    maze = Maze(level)
    player = Player(level)
    screen = pygame.display.set_mode(window_size)
    screen.fill(window_color)

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
        
        clock.tick(fps)
        if player.is_win == False:
            current_time = float(pygame.time.get_ticks() - start_time)/1000.0
        screen.fill(window_color)
        maze.draw_maze(screen,maze_height,maze_width,cell_size)
        player.draw_player(screen,cell_size)
        player.draw_time(screen,current_time)
        
        if player.is_win:
            if level_number==0:
                player.draw_end(screen)
            else:
                player.draw_win(screen)
            
        pygame.display.update()
        pygame.display.flip()
        