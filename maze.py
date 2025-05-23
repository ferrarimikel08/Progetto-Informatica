import pygame

class Maze:
    def __init__(self,file_name): #funzione init, leggiamo il file con la matrice (8X24)
        self.arrival_image = pygame.image.load("./immagini/arrivalpoint.png")
        self.path_image = pygame.image.load("./immagini/path.png")
        self.wall_image = pygame.image.load("./immagini/wall.png")
    
        
        
        matrix = []
        with open(file_name,"r",encoding="utf-8") as f:
            lines = f.readlines()
            for line in lines:
                matrix.append(line.split())
        self.maze = matrix
    
    def get_matrix_size(self): #funzione che ritorna una tupla con (n colonne, n righe)
        rows = len(self.maze)
        cols = len(self.maze[0])
        return (cols,rows)

    def draw_maze(self,screen,maze_height,maze_width,cell_size):
        end_color = (255,200,80)
        wall_color = (120,30,35)
        void_color = (200,55,60)
        self.arrival_image = pygame.transform.scale(self.arrival_image,(cell_size,cell_size))
        self.wall_image = pygame.transform.scale(self.wall_image,(cell_size,cell_size))
        self.path_image = pygame.transform.scale(self.path_image,(cell_size,cell_size))

        for y in range(maze_height):
            for x in range(maze_width):
                if self.maze[y][x] == '2':
                   # pygame.draw.rect(screen,wall_color,(x*cell_size,y*cell_size,cell_size,cell_size))
                    screen.blit(self.wall_image,(x*cell_size,y*cell_size,))
                if self.maze[y][x] == '0' or self.maze[y][x] == '1': 
                    #pygame.draw.rect(screen,void_color,(x*cell_size,y*cell_size,cell_size,cell_size))
                    screen.blit(self.path_image,(x*cell_size,y*cell_size,))
                if self.maze[y][x] == '3':
                    #pygame.draw.rect(screen,end_color,(x*cell_size,y*cell_size,cell_size,cell_size))
                    screen.blit(self.arrival_image,(x*cell_size,y*cell_size,))
    
    def draw_instructions(self,screen,is_paused=False):
        pygame.font.init()
        font1 = pygame.font.SysFont("Fantasy",40)
        instruction_color = (230,230,230)
        pause_text = "Premi P per mettere pausa"
        if is_paused:
            pause_text = "Premi P per togliere pausa"

            

        text_surface1 = font1.render("Porta l'endermen dal diamante",True,instruction_color)
        text_surface2 = font1.render("Usa le freccine per muoverti",True,instruction_color)
        text_surface3 = font1.render(pause_text,True,instruction_color)

        screen.blit(text_surface1,(600,450))
        screen.blit(text_surface2,(600,490))
        screen.blit(text_surface3,(600,530))


        
  
        