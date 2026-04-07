import pygame

class Map:
    def __init__(self):
        # 0 = herbe 1 = mur(bloqué)
        self.table = [
            [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
            [1, 0, 0, 0, 0, 0, 0, 0, 0, 1],
            [1, 0, 1, 1, 1, 1, 1, 1, 0, 1],
            [1, 0, 1, 0, 0, 0, 0, 1, 0, 1],
            [1, 0, 1, 0, 1, 1, 0, 1, 0, 1],
            [1, 0, 1, 0, 1, 1, 0, 1, 0, 1],
        ]
        self.sizeTile = 80 # carré 80x80 pixels
    
    def draw(self, surface):
        for indexLine, line in enumerate(self.table):
            for indexColumn, tile in enumerate(line):
                x = indexColumn * self.sizeTile
                y = indexLine * self.sizeTile
                
                #couleur de la tuile
                color = (50, 150, 50) if tile == 1 else (100, 100, 100)
                pygame.draw.rect(surface, color, (x, y, self.sizeTile, self.sizeTile))
                #bordure
                pygame.draw.rect(surface, (0, 0, 0), (x, y, self.sizeTile, self.sizeTile), 1)
                
                