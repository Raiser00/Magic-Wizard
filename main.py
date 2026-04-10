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

        if event.type == pygame.KEYDOWN:
            if gameState == "COMBAT":
                if event.key == pygame.K_c: # c pour capture
                    if currentMonster:
                        success = player.attemptCatch(currentMonster)
                        if success:
                            gameState = "EXPLORE"
                            currentMonster = None # on reinitialise

                #ajouter les autres actions de combat
    
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
        #zone du haut
        pygame.draw.rect(screen, (40, 60, 100), (0, 0, WIDTH, 400))
        pygame.draw.line(screen, (255, 255, 255), (0, 400), (WIDTH, 400), 5)


        # affichage du monstre
        # a update
        if currentMonster:
            # juste pour debug
            title = titleFont.render(f"Sauvage : {currentMonster.name} (Niv.{currentMonster.actualLevel}/{currentMonster.baseRank}) ", True, (255, 100, 100))
            stats = textFont.render(f"PV: {currentMonster.health}/{currentMonster.healthMax} | ATK: {currentMonster.atk} | DEF: {currentMonster.deff}", True, (255, 255, 255))
            screen.blit(title, (WIDTH - title.get_width() - 50, 50))
            screen.blit(stats, (WIDTH - stats.get_width() - 50, 100))

            # infos du joueur
            if player.ActiveCard:
                playerInfo = textFont.render(f"Ton monstre: {player.ActiveCard.name}", True, (100, 255, 100))
            else:
                playerInfo = textFont.render(f"Auncun monstre invoqué", True, (200, 200, 200))
            screen.blit(playerInfo, (50, 250))

            # zone du bas
            pygame.draw.rect(screen, (20, 20, 20), (0, 400, WIDTH, 200))

            attackOption = textFont.render("[A] Attaquer", True, (255, 255, 255))
            catchOption = textFont.render("[C] Capturer (Cartes: {player.emptyCard})", True, (255, 255, 255))
            echapOption = textFont.render("[F] Fuir", True, (255, 255, 255))

            # positionnement des options
            screen.blit(attackOption, (100, 450))
            screen.blit(catchOption, (350, 450))
            screen.blit(echapOption, (100, 520))   
            

            

    # mise à jour de l'affichage
    pygame.display.flip()
    clock.tick(60) # 60 images par seconde TRES IMPORTANT

pygame.quit()