import pygame
import time
import random

# Initialisation
pygame.init()
pygame.mixer.init()

# Sons
eat_sound = pygame.mixer.Sound("sounds/eat.mp3")
gameover_sound = pygame.mixer.Sound("sounds/gameover.mp3")

# Couleurs
blanc = (255, 255, 255)
noir = (0, 0, 0)
rouge = (213, 50, 80)
vert = (0, 255, 0)
bleu = (50, 153, 213)

# Fenêtre
largeur, hauteur = 600, 400
fenetre = pygame.display.set_mode((largeur, hauteur))
pygame.display.set_caption('🐍 Snake by Yahya')

# Horloge
horloge = pygame.time.Clock()

# Snake settings
taille_bloc = 10
vitesse = 15

# Police
font_style = pygame.font.SysFont("bahnschrift", 25)
score_font = pygame.font.SysFont("comicsansms", 20)

def afficher_score(score):
    value = score_font.render("Score: " + str(score), True, rouge)
    fenetre.blit(value, [0, 0])

def dessiner_snake(taille_bloc, liste_snake):
    for x in liste_snake:
        pygame.draw.rect(fenetre, vert, [x[0], x[1], taille_bloc, taille_bloc])

def message(msg, couleur):
    mesg = font_style.render(msg, True, couleur)
    fenetre.blit(mesg, [largeur / 6, hauteur / 3])

def game():
    game_over = False
    game_close = False

    x = largeur / 2
    y = hauteur / 2
    x_change = 0
    y_change = 0

    snake = []
    taille_snake = 1

    foodx = round(random.randrange(0, largeur - taille_bloc) / 10.0) * 10.0
    foody = round(random.randrange(0, hauteur - taille_bloc) / 10.0) * 10.0

    while not game_over:

        while game_close:
            fenetre.fill(noir)
            message("Tu as perdu ! Q pour quitter, C pour rejouer", rouge)
            afficher_score(taille_snake - 1)
            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        game_over = True
                        game_close = False
                    if event.key == pygame.K_c:
                        game()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x_change = -taille_bloc
                    y_change = 0
                elif event.key == pygame.K_RIGHT:
                    x_change = taille_bloc
                    y_change = 0
                elif event.key == pygame.K_UP:
                    y_change = -taille_bloc
                    x_change = 0
                elif event.key == pygame.K_DOWN:
                    y_change = taille_bloc
                    x_change = 0

        if x >= largeur or x < 0 or y >= hauteur or y < 0:
            gameover_sound.play()
            game_close = True

        x += x_change
        y += y_change
        fenetre.fill(bleu)
        pygame.draw.rect(fenetre, noir, [foodx, foody, taille_bloc, taille_bloc])
        snake_head = []
        snake_head.append(x)
        snake_head.append(y)
        snake.append(snake_head)
        if len(snake) > taille_snake:
            del snake[0]

        for segment in snake[:-1]:
            if segment == snake_head:
                gameover_sound.play()
                game_close = True

        dessiner_snake(taille_bloc, snake)
        afficher_score(taille_snake - 1)

        pygame.display.update()

        if x == foodx and y == foody:
            eat_sound.play()
            foodx = round(random.randrange(0, largeur - taille_bloc) / 10.0) * 10.0
            foody = round(random.randrange(0, hauteur - taille_bloc) / 10.0) * 10.0
            taille_snake += 1

        horloge.tick(vitesse)

    pygame.quit()
    quit()

game()
