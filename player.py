import pygame
from maze import Maze
class Player(Maze):
    def __init__(self, map_name):
      super().__init__(map_name)
      self.player_x, self.player_y = self.find_player()
      self.maze_height = len(self.maze)
      self.maze_width = len(self.maze[0])
      self.is_win = False

    def find_player(self):
        rows = len(self.maze)
        cols = len(self.maze[0]) 
        m = self.maze
        player_color = (255,0,0)

        for y in range(rows):
            for x in range(cols):
                if m[y][x] == '1':
                    return (x,y)

    def draw_player(self,screen,player_size):
        rows = len(self.maze)
        cols = len(self.maze[0]) 
        m = self.maze
        player_color = (255,0,0)

        for y in range(rows):
            for x in range(cols):
                if m[y][x] == '1':
                    pygame.draw.rect(screen,player_color,(x*player_size,y*player_size,player_size,player_size))

    def move_up(self):
        x = self.player_x
        y = self.player_y
        width = self.maze_width
        height = self.maze_height
        m = self.maze

        if y-1>=0 and m[y-1][x]=='0':
             m[y-1][x]='1'
             m[y][x]='0'
             self.player_y = y-1
        if y-1>=0 and m[y-1][x]=='3':
             m[y-1][x]='1'
             m[y][x]='0'
             self.player_y = y-1
             self.is_win=True


    def move_down(self):
        x = self.player_x
        y = self.player_y
        width = self.maze_width
        height = self.maze_height
        m = self.maze
        if y+1<height and m[y+1][x]=='0':
             m[y+1][x]='1'
             m[y][x]='0'
             self.player_y = y+1
        if y+1<height and m[y+1][x]=='3':
             m[y+1][x]='1'
             m[y][x]='0'
             self.player_y = y+1
             self.is_win = True
    
    def move_left(self):
        x = self.player_x
        y = self.player_y
        width = self.maze_width
        height = self.maze_height
        m = self.maze

        if x-1>=0 and m[y][x-1]=='0':
             m[y][x-1]='1'
             m[y][x]='0'
             self.player_x = x-1
        if x-1>=0 and m[y][x-1]=='3':
             m[y][x-1]='1'
             m[y][x]='0'
             self.player_x = x-1
             self.is_win = True
    
    
    def move_right(self):
        x = self.player_x
        y = self.player_y
        width = self.maze_width
        height = self.maze_height
        m = self.maze

        if x+1<width and m[y][x+1]=='0':
             m[y][x+1]='1'
             m[y][x]='0'
             self.player_x = x+1
        if x+1<width and m[y][x+1]=='3':
             m[y][x+1]='1'
             m[y][x]='0'
             self.player_x = x+1
             self.is_win = True

    def draw_win(self,screen,win_x,win_y):
        pygame.font.init()
        font = pygame.font.SysFont("Arial",70)
        win_color = (176,0,142)
        print("aaa")
        text_surface = font.render("HAI VINTO",True,win_color)
        screen.blit(text_surface,(200,200))