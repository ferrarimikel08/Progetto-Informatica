import pygame
from maze import Maze
class Player(Maze):
    def __init__(self, map_name):
      super().__init__(map_name)
      self.player_x, self.player_y = self.find_player()

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
