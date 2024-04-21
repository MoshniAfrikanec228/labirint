#создай игру "Лабиринт
from pygame import *
init()
win_width = 700
win_height = 500
window = display.set_mode((win_width, win_height))
display.set_caption("Maze")
bg = image.load('background.jpg')
clock = time.Clock()
fps = 1000

run = True

mixer.init()
mixer.music.load('koster-36181.ogg')
mixer.music.play()

class GameSprite(sprite.Sprite):
    def __init__(self,img,x,y,speed):
        super().__init__()
        self.image = image.load(img)
        self.image = transform.scale(self.image,(55,55))

        self.speed = speed

        self.naprv = "left"
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

    def show_s(self):
        window.blit(self.image, (self.rect.x, self.rect.y))

class Hero(GameSprite):
    def dvij(self):
        keys = key.get_pressed()
        if keys[K_w] and self.rect.y > 10:
            self.rect.y -= self.speed
        if keys[K_s] and self.rect.y < win_height- 60:
            self.rect.y += self.speed
        if keys[K_a] and self.rect.x  > 10:
            self.rect.x -= self.speed
        if keys[K_d] and self.rect.x < win_width - 60:
            self.rect.x += self.speed

class Vrag(GameSprite):
    def dvizh(self):
        if self.rect.x < 300:
            self.naprv = "right"
        elif self.rect.x > 600:
            self.naprv = 'left'
        if self.naprv == "left":
            self.rect.x -= self.speed
        if self.naprv == "right":
            self.rect.x += self.speed

class stena(sprite.Sprite):
    def __init__(self, x,y, w,h, r,g,b):
        super().__init__()
        self.stena = Surface((w, h))
        self.stena.fill((r,g,b))
        self.stena_rect = self.stena.get_rect()
        self.stena_rect.x = x
        self.stena_rect.y = y

    def show_s(self):
            window.blit(self.stena, (self.stena_rect.x, self.stena_rect.y))




player = Hero("hero.png", 20, 400, 5)
player1 = Vrag("hero.png", 20, 400, 5)
stena1 = stena(400, 490, 200, 300, 255, 255, 255)
stena2 = stena(470, 160, 10, 200, 255, 255, 255)
stena3 = stena(330, 160, 10, 200, 255, 255, 255)
stena4 = stena(260, 160, 10, 200, 255, 255, 255)
stena5 = stena(540, 160, 10, 200, 255, 255, 255)
stena6 = stena(610, 160, 10, 200, 255, 255, 255)
while run:
    for i in event.get():
        if i.type == QUIT:
            run = False
    display.update()
    clock.tick(fps)
    
    window.blit(bg, (0,0))

    player.show_s()
    player.dvij()
    player1.show_s()
    player1.dvizh()
    stena1.show_s()
    stena2.show_s()
    stena3.show_s()
    stena4.show_s()
    stena5.show_s()
    stena6.show_s()
    if sprite.collide_rect(player, player1):
        player = Hero("hero.png",20, 400, 5)
    if stena1.stena_rect.colliderect(player) or  stena2.stena_rect.colliderect(player) or stena3.stena_rect.colliderect(player) or stena4.stena_rect.colliderect(player) or stena5.stena_rect.colliderect(player) or stena6.stena_rect.colliderect(player):
        player = Hero("hero.png",20, 400, 5)
    display.update()


    clock.tick(fps)

















































































































































































































