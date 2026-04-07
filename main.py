import pygame
from entities import Character
from map import Map

pygame.init()


# fenetre
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Magic & Wizard")

# creation du héros
player = Character("Mani", 100)
# creation de la map
game_map = Map()

# boucle de jeu
running = True
clock = pygame.time.Clock() # stab la vitesse de jeu (de la boucle)
while running:
    # gestion des événements
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    ctrl = pygame.key.get_pressed()
    pace = 2

    if ctrl[pygame.K_LEFT]:
        player.position[0] -= pace
    if ctrl[pygame.K_RIGHT]:
        player.position[0] += pace
    if ctrl[pygame.K_UP]:
        player.position[1] -= pace
    if ctrl[pygame.K_DOWN]:
        player.position[1] += pace
    
    # dessin
    screen.fill((30, 30, 30))  # fond noir

    game_map.draw(screen) # dessin de la map

    # carre representant le joueur
    pygame.draw.rect(screen, (0, 255, 0), (player.position[0], player.position[1], 40, 40))

    # mise à jour de l'affichage
    pygame.display.flip()
    clock.tick(60) # 60 images par seconde TRES IMPORTANT

pygame.quit()