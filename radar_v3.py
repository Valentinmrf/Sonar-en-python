import pygame, sys
from pygame.locals import *
import math
import time
import random

pygame.init()
fenetre = pygame.display.set_mode((600, 600))
sonar = pygame.image.load("sonar.png").convert_alpha()
sonar = pygame.transform.scale(sonar, (600, 600))


transparente = pygame.Surface((600, 600), pygame.SRCALPHA)

#---------- Calcul du centre de la fenetre ----------
largeur, hauteur = fenetre.get_size()
capteur_x = largeur // 2
capteur_y = hauteur // 2
position_perso = sonar.get_rect(center=(capteur_x, capteur_y))

angle = -90
distance = 200

dernier_temps_detection = 0

#---------- Obstacle ----------
obstacles = []
chrono = 0
for i in range(3):
    angle_obstacle_random = random.randint(0, 360); print("angle_obstacle_random"); print(angle_obstacle_random)
    distance_obstacle_random = random.randint(0, 200); print("distance_obstacle_random"); print(distance_obstacle_random)

    x_obstacle = int(capteur_x + distance_obstacle_random * math.cos(math.radians(angle_obstacle_random)))
    y_obstacle = int(capteur_y + distance_obstacle_random * math.sin(math.radians(angle_obstacle_random)))

    obstacle = {
        "x": x_obstacle,
        "y": y_obstacle,
        "chrono": 0
    }
    obstacles.append(obstacle)
    print("obstacles: "); print(obstacles)
#---------- Début du programme ----------
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
        
        x_trainee = capteur_x + distance * math.cos(math.radians(angle_trainee))
        y_trainee = capteur_y + distance * math.sin(math.radians(angle_trainee))

        vert_trainee = int(225 - i*(225/70))
        opacite = int(225 - i * (225/70))
        pygame.draw.line(transparente, [0, vert_trainee, 30, opacite], (capteur_x, capteur_y), (x_trainee, y_trainee), 3)

#---------- Détection des obstacles --------
    angles = []
    for i in range(3):
        dx = obstacles[i]["x"] - capteur_x
        dy = obstacles[i]["y"] - capteur_y
        angle_obstacle = math.atan2(dy, dx)
        angle_obstacle = int(math.degrees(angle_obstacle))

        if angle_obstacle < 0 :
            angle_obstacle += 360

        angles.append(angle_obstacle)
        #print(angles)

        if abs(angle - angles[i]) < 1:
            obstacles[i]["chrono"] = time.time()

        if time.time() - obstacles[i]["chrono"] < 1:
            pygame.draw.circle(fenetre, [255, 0, 0], (obstacles[i]["x"], obstacles[i]["y"]), 7)

    pygame.display.flip()
