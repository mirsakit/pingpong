from pygame import *
from random import randint
mixer.init()
font.init()
from time import time as timer

win = display.set_mode((700, 500))
display.set_caption('Shooter')
lost = 0
font = font.SysFont('Arial', 50)
background = transform.scale(image.load('fon.jpg'), (700, 500))
clock = time.Clock()
FPS = 80

class GameSprite(sprite.Sprite):
    def __init__(self, player_image, x, y, sixe_x, size_y, speed_x, speed_y):
        super().__init__()
        self.image = transform.scale(image.load(player_image), (sixe_x, size_y))
        self.speed_y = speed_y
        self.speed_x = speed_x
        self.rect = self.image.get_rect()
        self.rect.x =  x
        self.rect.y =  y
    def reset(self):
        win.blit(self.image, (self.rect.x, self.rect.y))

class Line1(GameSprite):
    def update(self):
        keys_pressed = key.get_pressed()
        if keys_pressed[K_w]:
            self.rect.y -= self.speed_y
        if keys_pressed[K_s]:
            self.rect.y += self.speed_y
    

class Line2(GameSprite):
    def update(self):
        keys_pressed = key.get_pressed()
        if keys_pressed[K_UP]:
            self.rect.y -= self.speed_y
        if keys_pressed[K_DOWN]:
            self.rect.y += self.speed_y

class Ball(GameSprite):
    def update(self):
        self.rect.x+=self.speed_x
        self.rect.y+=self.speed_y
        if sprite.collide_rect(ball, line2) or sprite.collide_rect(ball, line1):
            self.speed_x*=-1
        if self.rect.y<=10 or self.rect.y>=460:
            self.speed_y*=-1

font1 = font.render('First player won!!', True, (255,255,255))
font2 = font.render('Second player won!!', True, (255,255,255))
 
line1 = Line1('line.png', 10, 100, 30, 130, 0, 7)
line2 = Line2('line1.png', 660, 100, 30, 130, 0, 7)
ball = Ball('ball.png', 300, 100, 50, 50, 4, 4)
game = True
finish = False
while game:
    
    for e in event.get():
        keys_pressed = key.get_pressed()
        
        if e.type == QUIT:
            game = False
    if finish != True:
        win.blit(background, (0, 0))
        
        line1.reset()
        line1.update()
        line2.reset()
        line2.update()
        ball.reset()
        ball.update()

        if ball.rect.x>730:
            win.blit(font1, (200, 200))
            finish = True
        if ball.rect.x<-60:
            win.blit(font2, (200, 200))
            finish = True

    clock.tick(FPS)
    display.update()
