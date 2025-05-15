import pygame

class Maze:

    def __init__(self,file_name):
        matrix = []
        with open(file_name,"r",encoding="utf-8") as f:
            lines = f.readlines()
            for line in lines:
                matrix.append(line.split())

        self.maze = matrix
    
    def get_matrix_size(self):
        rows = len(self.maze)
        cols = len(self.maze[0])
        return (cols,rows)


    def draw_maze(self,screen,maze_height,maze_width,cell_size,wall_color,void_color):
        
        for x in range(maze_height):
            for y in range(maze_width):
                if self.maze[x][y] == '2':
                    pygame.draw.rect(screen,wall_color,(x*cell_size,y*cell_size,cell_size,cell_size))
                if self.maze[x][y]== '0': 
                    pygame.draw.rect(screen,void_color,(x*cell_size,y*cell_size,cell_size,cell_size))

