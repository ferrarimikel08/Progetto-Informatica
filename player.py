import pygame

from maze import Maze
class Player(Maze):
    
    def __init__(self, map_name):
      super().__init__(map_name)
      self.player_x, self.player_y = self.find_player()
      self.maze_height = len(self.maze)
      self.maze_width = len(self.maze[0])
      self.is_win = False
      self.player_image = pygame.image.load("./immagini/character.png")

    def find_player(self):
        rows = len(self.maze)
        cols = len(self.maze[0]) 
        m = self.maze
        player_color = (255,0,0)

        for y in range(rows):
            for x in range(cols):
                if m[y][x] == '1':
                    return (x,y)

    def draw_player(self,screen,player_size): #spostare questa funzione insieme agli altri draw
        rows = len(self.maze)
        cols = len(self.maze[0]) 
        m = self.maze
        player_color = (255,0,0)
        self.player_image = pygame.transform.scale(self.player_image,(player_size,player_size))

        for y in range(rows):
            for x in range(cols):
                if m[y][x] == '1':
                    #pygame.draw.rect(screen,player_color,(x*player_size,y*player_size,player_size,player_size))\
                    screen.blit(self.player_image,(x*player_size,y*player_size))


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
    
    def update_records(self,times):
        level_number = 0
        records = self.get_records()
        for time in times:
            if len(records)>level_number:
                records[level_number] = min(records[level_number],time)
            else:
                records.append(time)
            level_number+=1
        with open("records.txt","w") as f:
            for r in records:
                f.write(str(r)+"\n")

    
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

    def draw_win(self,screen):        
        pygame.font.init()
        font1 = pygame.font.SysFont("impact",60)
        font2 = pygame.font.SysFont("impact", 40)
        win_color = (255,255,255)
        text_surface1 = font1.render("HAI COMPLETATO IL LIVELLO",True,win_color)
        text_surface2 = font2.render('PREMERE "INVIO" PER PASSARE AL PROSSIMO LIVELLO',True,win_color)                        
        screen.blit(text_surface1,(300,400))
        screen.blit(text_surface2,(200,465))
    
    def draw_end(self,screen, times):
        pygame.font.init()
        font1 = pygame.font.SysFont("impact", 80)
        font2 = pygame.font.SysFont("impact", 40)
        font3 = pygame.font.SysFont("impact", 15)
        win_color = (255,255,255)
        text_surface1 = font1.render("HAI COMPLETATO IL GIOCO",True,win_color)
        text_surface2 = font2.render('PREMERE "INVIO" PER VEDERE I TUOI RECORD',True,win_color)                        
        screen.blit(text_surface1,(100,120))
        screen.blit(text_surface2,(170,200))

        level_number = 0
        records = self.get_records()
        for time in times:
            
            text = "LIVELLO "+str(level_number)+": "+str(time)+" RECORD: "+str(records[level_number])
            text_surface3 = font3.render(text,True,win_color)
            ypos = 290+20*level_number
            screen.blit(text_surface3,(600,ypos))
            level_number=level_number+1

    def draw_time(self,screen,time):
        pygame.font.init()
        font1 = pygame.font.SysFont("impact",50)
        time_color = (255,255,255)
        text_surface1 = font1.render("TEMPO: "+str(time),True,time_color)
        screen.blit(text_surface1,(466,518))
    
    def get_records(self):
        records = []
        with open("records.txt", "r") as f:
            records = f.readlines()
            records = [float(r) for r in records if r.strip() != ""]
        return records
