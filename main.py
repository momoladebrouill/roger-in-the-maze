import pygame

pygame.init()

f = pygame.display.set_mode((500, 500),pygame.RESIZABLE)
pygame.display.set_caption("Robert se perd dans un labyrinthe coloré", "ryan stp répond")
pygame.display.set_icon(pygame.image.load("greuch.png"))
grenouille = pygame.image.load("greuch.png")
greuch = pygame.transform.scale(grenouille, (50, 50))
maze = pygame.transform.scale(pygame.image.load("maze(5).png"), (3000, 3000))
bg = pygame.transform.scale(pygame.image.load("fond noir.png"), (3000, 3000))
presser = {}


def kiss_check(sprite, group):
    return pygame.sprite.spritecollide(sprite, group, False, pygame.sprite.collide_mask)


class Joueur(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = greuch
        self.vitesse = 10
        self.rect = self.image.get_rect()
        self.rect.x = 250
        self.rect.y = 250


class backg(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = bg
        self.rect = self.image.get_rect()
        self.rect.x = 0
        self.rect.y = 0


class Laby(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = maze
        self.vitesse = 10
        self.rect = self.image.get_rect()
        self.rect.x = -1500
        self.rect.y = -1500

    def droite(self):
        self.rect.x -= self.vitesse

    def gauche(self):
        self.rect.x += self.vitesse

    def up(self):
        self.rect.y += self.vitesse

    def down(self):
        self.rect.y -= self.vitesse


fonds = pygame.sprite.Group()
mazinger = Laby()
fonds.add(mazinger)
players = pygame.sprite.Group()
monique = Joueur()
players.add(monique)
fps=pygame.time.Clock()
boucle = True
while boucle:
    # actualiser:
    pygame.display.flip()
    fps.tick(60)
    # appliquer les images sur le jeu:
    f.blit(bg, (0,0) )
    f.blit(mazinger.image, mazinger.rect)

    # key listener
    if presser.get(pygame.K_RIGHT):
        mazinger.droite()
        if not f.get_at((int(monique.rect.x + monique.rect.width), int(monique.rect.y + monique.rect.height / 2))) == (
                255, 255, 255, 255):
            f.blit(mazinger.image, mazinger.rect)
            for j in range(1): 
                mazinger.gauche()
    elif presser.get(pygame.K_LEFT):
        mazinger.gauche()
        f.blit(mazinger.image, mazinger.rect)
        if not f.get_at((int(monique.rect.x), int(monique.rect.y + monique.rect.height / 2))) == (
                255, 255, 255, 255):
            for j in range(1):
                mazinger.droite()
    elif presser.get(pygame.K_UP):
        mazinger.up()
        f.blit(mazinger.image, mazinger.rect)
        if not f.get_at((int(monique.rect.x + monique.rect.width / 2), int(monique.rect.y))) == (
                255, 255, 255, 255):
            for j in range(1):
                mazinger.down()
    elif presser.get(pygame.K_DOWN):
        mazinger.down()
        f.blit(mazinger.image, mazinger.rect)
        if not f.get_at((int(monique.rect.x + monique.rect.width / 2), int(monique.rect.y + monique.rect.height))) == (
                255, 255, 255, 255):
            for j in range(1):
                mazinger.up()
    elif presser.get(pygame.K_SPACE):
        if mazinger.vitesse==10:
            mazinger.vitesse=25
        else:
            mazinger.vitesse=10

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            boucle = False  # la boucle n'est plus vraie dons on arrete de trourner
            print("fin du jeu")
            pygame.quit()  # fermeture de fenetre
        # si une touche a été relaché
        elif event.type == pygame.KEYDOWN:
            presser[event.key] = True
        elif event.type == pygame.KEYUP:
            presser[event.key] = False
    f.blit(monique.image, monique.rect)
