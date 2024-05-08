from pygame import *
from random import randint
mixer.init()
font.init()
from time import time as timer

win = display.set_mode((700, 500))
display.set_caption('Shooter')
lost = 0
font1 = font.SysFont('Arial', 36)
font2 = font.SysFont('Arial', 36)
font_win = font.SysFont('Arial', 100)
background = transform.scale(image.load('fon.jpg'), (700, 500))
clock = time.Clock()
FPS = 60

class GameSprite(sprite.Sprite):
    def __init__(self, player_image, x, y, sixe_x, size_y, speed):
        super().__init__()
        self.image = transform.scale(image.load(player_image), (sixe_x, size_y))
        self.speed = speed
        self.rect = self.image.get_rect()
        self.rect.x =  x
        self.rect.y =  y
    def reset(self):
        win.blit(self.image, (self.rect.x, self.rect.y))

class Line1(GameSprite):
    def update(self):
        keys_pressed = key.get_pressed()
        if keys_pressed[K_w]:
            self.rect.y -= self.speed
        if keys_pressed[K_s]:
            self.rect.y += self.speed
    

class Line2(GameSprite):
    def update(self):
        keys_pressed = key.get_pressed()
        if keys_pressed[K_UP]:
            self.rect.y -= self.speed
        if keys_pressed[K_DOWN]:
            self.rect.y += self.speed

class Ball(GameSprite):
    def update(self):
        self.rect.x+=self.speed
        self.rect.y-=self.speed
        if sprite.collide_rect(ball, line2) or sprite.collide_rect(ball, line1):
            self.speed*=-1
        if self.rect.y<=0 or self.rect.y>=500:
            self.rect.y+=self.speed

 
line1 = Line1('line.png', 10, 100, 30, 130, 7)
line2 = Line2('line1.png', 660, 100, 30, 130, 7)
ball = Ball('ball.png', 300, 100, 50, 50, 5)
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
        
        

    clock.tick(FPS)
    display.update()
