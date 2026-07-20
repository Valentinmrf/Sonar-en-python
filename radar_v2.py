import pygame, sys
from pygame.locals import *
import math
import time

pygame.init()
fenetre = pygame.display.set_mode((600, 600))
sonar = pygame.image.load("sonar.png").convert_alpha()
sonar = pygame.transform.scale(sonar, (600, 600))


transparente = pygame.Surface((600, 600), pygame.SRCALPHA)

#---------- Calcul du centre de la fenetre ----------
largeur, hauteur = fenetre.get_size()
capteur_x = largeur // 2; print("capteur_x = ", capteur_x )
capteur_y = hauteur // 2; print("capteur_y = ", capteur_y )
position_perso = sonar.get_rect(center=(capteur_x, capteur_y))

angle = -90
distance = 200

dernier_temps_detection = 0

#---------- Obstacle ----------
obstacle_x = 400 
obstacle_y = 200

running = True
while running :
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

#---------- Aiguille ---------
    angle += 0.15
    if angle >= 360:
        angle -= 360
    x2 = capteur_x + distance * math.cos(math.radians(angle))
    y2 = capteur_y + distance * math.sin(math.radians(angle))

    fenetre.blit(sonar, position_perso)
    aiguille = pygame.draw.line(fenetre, [0, 225, 75], (capteur_x, capteur_y), (x2, y2), 3)

#---------- Trainée de l'aiguille ----------
    fenetre.blit(transparente, (0, 0))
    for i in range(70):
        angle_trainee = angle - 0.5 * i
        print(angle_trainee)
        
        x_trainee = capteur_x + distance * math.cos(math.radians(angle_trainee))
        y_trainee = capteur_y + distance * math.sin(math.radians(angle_trainee))

        vert_trainee = int(225 - i*(225/70))
        opacite = int(225 - i * (225/70))
        pygame.draw.line(transparente, [0, vert_trainee, 30, opacite], (capteur_x, capteur_y), (x_trainee, y_trainee), 3)

#---------- Détection des obstacles --------
    dx = obstacle_x - capteur_x
    dy = obstacle_y - capteur_y
    angle_obstacle = math.atan2(dy, dx)
    angle_obstacle = math.degrees(angle_obstacle)

    if angle_obstacle < 0 :
        angle_obstacle += 360

    if abs(angle - angle_obstacle) < 1:
        dernier_temps_detection = time.time()
    
    if time.time() - dernier_temps_detection < 1 :
        pygame.draw.circle(fenetre, [255, 0, 0], (obstacle_x, obstacle_y), 7)

    pygame.display.flip()
