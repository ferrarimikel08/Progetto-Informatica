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
        font1 = pygame.font.SysFont("impact",40)
        font2 = pygame.font.SysFont("impact",20)
        instruction_color = (230,230,230)
        pause_text = "PREMERE P PER METTERE IN PAUSA"
        if is_paused:
            pause_text = "PREMERE P PER RIPRENDERE"
        text_surface1 = font1.render("PORTA L'ENDERMAN AL DIAMANTE",True,instruction_color)
        text_surface2 = font2.render("USA LE FRECCINE PER MUOVERTI NELLA LAVA",True,instruction_color)
        text_surface3 = font2.render(pause_text,True,instruction_color)

        screen.blit(text_surface1,(350,400))
        screen.blit(text_surface2,(430,450))
        screen.blit(text_surface3,(465,480))        