# Sonar-en-python
Le programme simule un capteur fixe placé au centre de l'écran. Une aiguille balaye la zone en continu, comme un radar rotatif. À chaque frame, l'angle de l'aiguille est comparé à l'angle entre le capteur et l'obstacle (calculé avec math.atan2) : quand les deux angles coïncident, l'obstacle est considéré comme détecté et reste affiché pendant environ 1 seconde, pour rester visible malgré la vitesse de balayage.

Dans cette première version, un seul obstacle est géré, à des coordonnées fixes écrites directement dans le code (facilement modifiables).

Dans la 2ème version, le système d'obstacle n'a pas changé. Les seuls changement sont visuel, l'ajout d'une trainée derrière l'aiguille en réalisant un dégradée de la couleur de l'aiguille ainsi qu'un dégradé de l'opacité.
