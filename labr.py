from typing import Any
import pygame as pg

window = pg.display.set_mode((700,500))
pg.display.set_caption('Fastcliccer')
window.fill((0,155,255))

class spr(pg.sprite.Sprite):
    def __init__(self,img,play_x,play_y,size_x,size_y):
        pg.sprite.Sprite()
        self.image = pg.transform.scale(pg.image.load(img),(size_x,size_y))
        self.rect = self.image.get_rect()
        self.rect.x = play_x
        self.rect.y = play_y

    def reset(self):
        window.blit(self.image,(self.rect.x,self.rect.y))
    
class Player(spr):
    def __init__(self, img, play_x, play_y, size_x, size_y,play_speed_x,play_speed_y):
        spr().__init__(self,img, play_x, play_y, size_x, size_y)
        self.x_sp = play_speed_x
        self.y_sp = play_speed_y
    
    def update(self):
        self.rect.x += self.x_sp
        self.rect.y += self.y_sp

w1 = spr('ocr.jpeg',100,100,100,200)
w2 = spr('ocr.jpeg',100,150,300,100)
pac = Player('png.png',0,0,50,50,0,0)
game = True
while game:
    for e in pg.event.get():
        if e.type == pg.QUIT:
            game = False
    for e in pg.event.get():
        if e.type == pg.K_UP:
            if e.type == pg.KEYDOWN:
                pac.play_speed_y += 3
            if e.type == pg.KEYUP:
                pac.play_speed_y = 0
        elif e.type == pg.K_DOWN:
            if e.type == pg.KEYDOWN:
                pac.play_speed_y -= 3
            if e.type == pg.KEYUP:
                pac.play_speed_y = 0
        elif e.type == pg.K_LEFT:
            if e.type == pg.KEYDOWN:
                pac.play_speed_x -= 3
            if e.type == pg.KEYUP:
                pac.play_speed_x = 0
        elif e.type == pg.K_RIGHT:
            if e.type == pg.KEYDOWN:
                pac.play_speed_x += 3
            if e.type == pg.KEYUP:
                pac.play_speed_x = 0
    pac.reset()
    w1.reset()
    w2.reset()
    pg.display.update()
    pg.time.delay(25)