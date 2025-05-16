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


    def draw_maze(self,screen,maze_height,maze_width,cell_size):
        end_color = (0,255,0)
        wall_color = (0,0,255)
        void_color = (255,255,255)

        for y in range(maze_height):
            for x in range(maze_width):
                if self.maze[y][x] == '2':
                    pygame.draw.rect(screen,wall_color,(x*cell_size,y*cell_size,cell_size,cell_size))
                if self.maze[y][x] == '0' or self.maze[y][x] == '1': 
                    pygame.draw.rect(screen,void_color,(x*cell_size,y*cell_size,cell_size,cell_size))
                if self.maze[y][x] == '3':
                    pygame.draw.rect(screen,end_color,(x*cell_size,y*cell_size,cell_size,cell_size))
        
        def get_player_pos(self):
            rows = len(self.maze)
            cols = len(self.maze[0]) 
            m = self.maze
            for y in range(rows):
                for x in range(cols):
                    if m[y][x] == '1':
                        return (x,y)
        