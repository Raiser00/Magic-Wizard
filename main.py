import pygame
import random
from entities import Character, Monster, Card
from database import CATALOGUE_MONSTRES
from map import Map

pygame.init()

##init des polices
titleFont = pygame.font.SysFont("Arial", 36, bold=True)
textFont = pygame.font.SysFont("Arial", 24)


currentMonster = None


# fenetre
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Magic & Wizard")

# etat du jeu
gameState = "EXPLORE"

# creation du héros
player = Character("Mani", 100)
# creation de la map
gameMap = Map()

# boucle de jeu
running = True
clock = pygame.time.Clock() # stab la vitesse de jeu (de la boucle)

while running:
    # gestion des événements
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    if gameState == "EXPLORE":
        ctrl = pygame.key.get_pressed()
        pace = 2
        next_x = player.position[0]
        next_y = player.position[1]



        if ctrl[pygame.K_LEFT]:
            next_x -= pace
        if ctrl[pygame.K_RIGHT]:
            next_x += pace
        if ctrl[pygame.K_UP]:
            next_y -= pace
        if ctrl[pygame.K_DOWN]:
            next_y += pace

        if gameMap.isBlocked(next_x, next_y) and \
            gameMap.isBlocked(next_x + 39, next_y) and \
            gameMap.isBlocked(next_x, next_y + 39) and \
            gameMap.isBlocked(next_x + 39, next_y + 39):
    
    # vérifier si la nouvelle position est valide
            player.position[0] = next_x
            player.position[1] = next_y
            
            tile_x = (player.position[0] + 20) // gameMap.sizeTile
            tile_y = (player.position[1] + 20) // gameMap.sizeTile
            
            if gameMap.table[tile_y][tile_x] == 2:
                if random.randint(1, 100) == 1: # 30% de chance de combat
                    print("Combat!")

                    randomMonster = random.choice(list(CATALOGUE_MONSTRES.keys()))
                    data = CATALOGUE_MONSTRES[randomMonster]

                    currentMonster = Monster(randomMonster, data["atk"], data["def"], data["rank"])


                    gameState = "COMBAT"

    # dessin
    screen.fill((30, 30, 30))  # fond noir
    
    if gameState == "EXPLORE":
        gameMap.draw(screen) # dessin de la map
        # dessin du joueur
        pygame.draw.rect(screen, (0, 255, 0), (player.position[0], player.position[1], 40, 40))

    elif gameState == "COMBAT":
        screen.fill((0, 0, 150))

        # affichage du monstre
        # a update
        if currentMonster:
            # juste pour debug
            title = titleFont.render(f"Sauvage : {currentMonster.name} (Niv.{currentMonster.actualLevel}/{currentMonster.baseRank}) ", True, (255, 255, 255))
            stats = textFont.render(f"ATK: {currentMonster.atk} | DEF: {currentMonster.deff}", True, (200, 200, 255))
            hp = textFont.render(f"HP: {currentMonster.health}/{currentMonster.healthMax}", True, (50, 255, 50))

            playerInfo = textFont.render(f"Tes cartes vides: {player.emptyCard} ", True, (255, 255, 255))
            action = textFont.render("Appuyez sur C pour capturer", True, (255, 255, 255))

            # affichage
            screen.blit(playerInfo, (50, 450))
            screen.blit(action, (50, 500))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_c:  # c pour capture
                    success = player.attemptCatch(currentMonster)
                    if success:
                        gameState = "EXPLORE"

    # mise à jour de l'affichage
    pygame.display.flip()
    clock.tick(60) # 60 images par seconde TRES IMPORTANT

pygame.quit()