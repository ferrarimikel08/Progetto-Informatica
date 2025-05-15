import pygame

class Maze:

    def __init__(self,screen,file_name):
        matrix = []
        with open(file_name,"r",encoding="utf-8") as f:
            lines = f.readlines()
            for line in lines:
                matrix.append(line.split())

        self.maze = matrix
    
