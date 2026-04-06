import pygame
from entities import Character

pygame.init()


# fenetre
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Magic & Wizard")

# creation du héros
player = Character("Mani", 100)

# boucle de jeu
running = True
while running:
    # gestion des événements
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    # dessin
    screen.fill((30, 30, 30))  # fond noir

    # carre representant le joueur
    pygame.draw.rect(screen, (0, 255, 0), (player.position[0], player.position[1], 40, 40))

    # mise à jour de l'affichage
    pygame.display.flip()

pygame.quit()