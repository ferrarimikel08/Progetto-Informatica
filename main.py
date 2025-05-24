import pygame,sys
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
levels = ["gamemap1.txt", "gamemap2.txt","gamemap3.txt","gamemap4.txt","gamemap5.txt"]
times = []

level_number = len(levels)
for level in levels:
    time_registered = False
    current_time = 0
    first_input = True
    level_number = level_number-1
    is_paused = False
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

            if event.type == pygame.KEYDOWN and player.is_win==False:  
                if first_input == True:
                    start_time = pygame.time.get_ticks()
                    first_input = False
                    time = 0

                if event.key==pygame.K_LEFT and not is_paused:
                    player.move_left()
                elif event.key==pygame.K_RIGHT and not is_paused:
                    player.move_right()
                elif event.key==pygame.K_UP and not is_paused: #mettere spazi agli uguali
                    player.move_up()
                elif event.key == pygame.K_DOWN and not is_paused: #sostituire cond==False con not cond
                    player.move_down()
                elif event.key == pygame.K_p:
                    if is_paused == False:
                        is_paused = True
                        pause_start = pygame.time.get_ticks()
                    else:
                        is_paused = False
                        total_paused_time += pygame.time.get_ticks() - pause_start

            elif event.type == pygame.KEYDOWN and player.is_win==True:
                if event.key == pygame.K_RETURN:
                    play = False
        
        clock.tick(fps)
        if player.is_win == False and first_input==False and is_paused == False:
            current_time = float(pygame.time.get_ticks() - start_time - total_paused_time)/1000.0
        maze.draw_maze(screen,maze_height,maze_width,cell_size)
        if player.is_win==False:
            maze.draw_instructions(screen,is_paused)
        player.draw_player(screen,cell_size)
        player.draw_time(screen,current_time)
        
        if player.is_win:
            if time_registered==False:
                times.append(current_time)
                time_registered=True

            if level_number==0:
                player.update_records(times)
                player.draw_end(screen,times)
            else:
                player.draw_win(screen)
            
        pygame.display.update()

if level_number == 0:
    showing_records = True
    while showing_records:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN and event.key == pygame.K_RETURN:
                showing_records = False

        screen.blit(background_image, (0, 0))
        player.draw_end(screen, times)
        pygame.display.update()

        
        