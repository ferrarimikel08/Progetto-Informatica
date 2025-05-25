import pygame, sys
from pygame.locals import *

from maze import Maze
from player import Player

pygame.init()

window_width = 1200
window_height = 600
window_size = (window_width,window_height)
window_color = (120,30,35)
BLACK = (0,0,0)

pygame.display.set_caption("Labirinto")

background_image = pygame.image.load("./immagini/background.png")
background_image = pygame.transform.scale(background_image, window_size)

clock = pygame.time.Clock()
fps = 30

cell_size = 50

levels = ["./gamemaps/gamemap1.txt", "./gamemaps/gamemap2.txt", "./gamemaps/gamemap3.txt","./gamemaps/gamemap4.txt", "./gamemaps/gamemap5.txt",]

times = []

level_number = len(levels)
for level in levels:
    is_paused = False
    time_registered = False
    first_input = True
    current_time = 0
    level_number = level_number - 1
    pause_start = 0
    total_paused_time = 0

    maze = Maze(level)
    player = Player(level)

    screen = pygame.display.set_mode(window_size)
    screen.fill(window_color)

    maze_width, maze_height = maze.get_matrix_size()

    play = True

    while play:
        screen.blit(background_image, (0, 0))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.display.quit()
                pygame.quit()
                sys.exit()

            if event.type == pygame.KEYDOWN and player.is_win == False:  
                if first_input == True:
                    start_time = pygame.time.get_ticks()
                    first_input = False
                    time = 0

                if event.key == pygame.K_LEFT and not is_paused:
                    player.move_left()
                elif event.key == pygame.K_RIGHT and not is_paused:
                    player.move_right()
                elif event.key == pygame.K_UP and not is_paused: 
                    player.move_up()
                elif event.key == pygame.K_DOWN and not is_paused: 
                    player.move_down()
                elif event.key == pygame.K_p:
                    if not is_paused:
                        is_paused = True
                        pause_start = pygame.time.get_ticks()
                    else:
                        is_paused = False
                        total_paused_time += pygame.time.get_ticks() - pause_start

            elif event.type == pygame.KEYDOWN and player.is_win == True:
                if event.key == pygame.K_RETURN:
                    if level_number == 0:
                        player.draw_records(screen, times, background_image)
                        level_number = -1
                    else:
                        play = False
        
        clock.tick(fps)

        if player.is_win == False and first_input == False and not is_paused:
            current_time = float(pygame.time.get_ticks() - start_time - total_paused_time) / 1000.0

        maze.draw_maze(screen, maze_height, maze_width, cell_size)

        if player.is_win == False:
            maze.draw_instructions(screen, is_paused)
        
        player.draw_player(screen, cell_size)
        player.draw_time(screen, current_time)
        
        if player.is_win:
            if not time_registered:
                times.append(current_time)
                time_registered = True

            if level_number == 0:
                player.draw_end(screen)
            elif level_number == -1:
                player.update_records(times)
                player.draw_records(screen, times, background_image)
            else:
                player.draw_win(screen)
            
        pygame.display.update()        