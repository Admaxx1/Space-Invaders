import random
import math
import pygame
import threading

pygame.init()

screen = pygame.display.set_mode((800, 800))
In_Gh = False

def bg_music():
    pygame.mixer.music.load('13. Boss.mp3')
    pygame.mixer.music.play()

x = threading.Thread(target=bg_music)
x.start()

# CLASSES

class Invader:
    def __init__(self, image):
        self.Invader = image
        self.x = random.randint(0, 770)
        self.y = random.randint(0, 400)

    def show_invader(self):
        screen.blit(self.Invader, (self.x, self.y))

    def move_invader(self):
        if self.x < player_x:
            self.x += 0.1
        if self.x > player_x:
            self.x -= 0.1
        if self.y < player_y:
            self.y += 0.1
        if self.y > player_y:
            self.y -= 0.1

    def collision_Bullet(self, bX, bY):
        if (math.sqrt((math.pow(self.x - bX, 2)) + (math.pow(self.y - bY, 2)))) < 27:
            return True

    def collision_spaceShip(self,pX,pY):
        if (math.sqrt((math.pow(self.x - pX, 2)) + (math.pow(self.y - pY, 2)))) < 27:
            return True


class ghost(Invader):
    pass


class SpaceShip:
    def __init__(self, image, x, y, speed):
        self.Img = image
        self.x_coor = x
        self.y_coor = y
        self.change_speed = speed

    def show_SPACESHIP(self, xcoor):
        screen.blit(self.Img, (xcoor, self.y_coor))


class Bullet:
    global bullet_state

    def __init__(self, image):
        self.bullet = image
        self.x_coor = player_x + 20
        self.y_coor = 700

    def show(self):
        screen.blit(self.bullet, (self.x_coor, self.y_coor))

    def move(self):
        global bullet_state
        if self.y_coor <= 0:
            bullet_state = 'DISABLED'
        if bullet_state == 'ready':
            self.y_coor -= bullet_change


class Monster1(Invader):
    pass


class Monster2(Invader):
    pass


class Monster3(Invader):
    pass


class Monster4(Invader):
    pass


class Monster5(Invader):
    pass



# IMAGES

ghostImg = pygame.image.load('video.png')
spaceshipImg = pygame.image.load('space-invaders.png')
monster1 = pygame.image.load('monster (1).png')
monster2 = pygame.image.load('monster (2).png')
monster3 = pygame.image.load('monster (3).png')
monster4 = pygame.image.load('monster.png')
monster5 = pygame.image.load('cthulhu.png')

# VARIABLES

game_over = False
clock = pygame.time.Clock()
player_x = 370
player_y = 700
changeInX = 0
bullet_state = 'DISABLED'
score = 1
bullet_change = 1
Numone = False
Numtwo = False
Numthree = False
Numfour = False
Numfive = False
MONSTER1 = Monster1(monster1)
MONSTER2 = Monster1(monster2)
MONSTER3 = Monster1(monster3)
MONSTER4 = Monster1(monster4)
MONSTER5 = Monster1(monster5)
Ghost = ghost(ghostImg)
spaceship = SpaceShip(spaceshipImg, player_x, player_y, 0.3)
bullet = Bullet(pygame.image.load('bullet.png'))

while not game_over:

    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            pygame.quit()
            quit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                changeInX = -1
            if event.key == pygame.K_RIGHT:
                changeInX = 1
            if event.key == pygame.K_SPACE:
                if bullet_state == 'DISABLED':
                    bullet_state = 'ready'
                    bullet.x_coor = player_x + 20
                    bullet.y_coor = 700

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT:
                changeInX = -0
            if event.key == pygame.K_RIGHT:
                changeInX = 0

    # CONTINUOUSLY RUNNING STATEMENTS

    screen.fill('black')

    Ghost.move_invader()

    Ghost.show_invader()

    player_x += changeInX

    spaceship.show_SPACESHIP(player_x)

    # 'IF' STATEMENTS

    if Ghost.collision_Bullet(bullet.x_coor, bullet.y_coor) is True:
        score += 1
        Ghost.x = random.randint(0, 770)
        Ghost.y = random.randint(0, 400)

    if (score / 5).is_integer():
        Numone = True

    if (score / 7).is_integer():
        Numtwo = True

    if (score / 9).is_integer():
        Numthree = True

    if (score / 12).is_integer():
        Numfour = True

    if (score / 15).is_integer():
        Numfive = True

    if (score / 17).is_integer():
        Numsix = True

    if Ghost.collision_spaceShip(player_x,player_y) is True:
        game_over = True

    if Numone is True:
        clock.tick(1050)
        MONSTER1.show_invader()
        MONSTER1.move_invader()
        if MONSTER1.collision_Bullet(bullet.x_coor, bullet.y_coor) is True:
            MONSTER1.x = random.randint(0, 770)
            MONSTER1.y = random.randint(0, 400)
        if MONSTER1.collision_spaceShip(player_x, player_y) is True:
            game_over = True

    if Numtwo is True:
        clock.tick(1100)
        MONSTER2.show_invader()
        MONSTER2.move_invader()
        if MONSTER2.collision_Bullet(bullet.x_coor, bullet.y_coor) is True:
            MONSTER2.x = random.randint(0, 770)
            MONSTER2.y = random.randint(0, 400)
        if MONSTER2.collision_spaceShip(player_x, player_y) is True:
            game_over = True

    if Numthree is True:
        clock.tick(1150)
        MONSTER3.show_invader()
        MONSTER3.move_invader()
        if MONSTER3.collision_Bullet(bullet.x_coor, bullet.y_coor) is True:
            MONSTER3.x = random.randint(0, 770)
            MONSTER3.y = random.randint(0, 400)
        if MONSTER3.collision_spaceShip(player_x, player_y) is True:
            game_over = True

    if Numfour is True:
        clock.tick(1200)
        MONSTER4.show_invader()
        MONSTER4.move_invader()
        if MONSTER4.collision_Bullet(bullet.x_coor, bullet.y_coor) is True:
            MONSTER4.x = random.randint(0, 770)
            MONSTER4.y = random.randint(0, 400)
        if MONSTER4.collision_spaceShip(player_x, player_y) is True:
            game_over = True

    if Numfive is True:
        clock.tick(1300)
        MONSTER5.show_invader()
        MONSTER5.move_invader()
        if MONSTER5.collision_Bullet(bullet.x_coor, bullet.y_coor) is True:
            MONSTER5.x = random.randint(0, 770)
            MONSTER5.y = random.randint(0, 400)
        if MONSTER5.collision_spaceShip(player_x, player_y) is True:
            game_over = True



    if bullet_state == 'ready':
        bullet.move()
        bullet.show()

    if player_x <= 0:
        player_x = 0
    if player_x >= 740:
        player_x = 740

    # UPDATE LOOP

    pygame.display.update()

# MONSTER1 = Monster1(monster1)
# MONSTER2 = Monster1(monster2)
# MONSTER3 = Monster1(monster3)
# MONSTER4 = Monster1(monster4)
# MONSTER5 = Monster1(monster5)
# MONSTER6 = Monster1(monster6)
