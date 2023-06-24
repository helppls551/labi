from pygame import *

class GameSprite(sprite.Sprite):

    def __init__(self, player_image, player_x, player_y, size_x, size_y):
        sprite.Sprite.__init__(self)
        self.image = transform.scale(image.load(player_image), (size_x, size_y))
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y

    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))

class Player(GameSprite):
    def __init__(self, player_image, player_x, player_y, size_x, size_y, player_x_speed, player_y_speed):
        GameSprite.__init__(self, player_image, player_x, player_y, size_x, size_y)
        self.x_speed = player_x_speed
        self.y_speed = player_y_speed

    def update(self):
        # self.rect.x += self.x_speed
        # self.rect.y += self.y_speed
        if self.rect.x <= win_width-80 and self.x_speed > 0 or self.rect.x >= 0 and self.x_speed < 0:
            self.rect.x += self.x_speed
        platforms_touched = sprite.spritecollide(self, barriers ,False)
        if self.x_speed > 0:
            for p in platforms_touched:
                self.rect.right = p.rect.left
        elif self.x_speed < 0:
            for p in platforms_touched:
                self.rect.left = p.rect.right
        if self.rect.y <= win_height-80 and self.y_speed > 0 or self.rect.y >= 0 and self.y_speed < 0:
            self.rect.y += self.y_speed
        platforms_touched = sprite.spritecollide(self,barriers, False)
        if self.y_speed > 0:
            for p in platforms_touched:
                self.rect.bottom = p.rect.top
        elif self.y_speed < 0:
            for p in platforms_touched:
                self.rect.top = p.rect.bottom


win_width = 1240
win_height = 1040
window = display.set_mode((win_width, win_height))
display.set_caption("Лабиринт")
back = (119, 210, 223)
barriers = sprite.Group()
w1 = GameSprite('platform1.png',116, 250, 300, 50)
w2 = GameSprite('platform2.png', 370, 100, 50, 400)
w1_2 = GameSprite('platform1.png',924, 250, 300, 50)
w1_3 = GameSprite('platform1.png',724, 500, 300, 50)
w1_4 = GameSprite('platform1.png',1040, 700, 300, 50)
w1_5 = GameSprite('platform1.png',724, 900, 300, 50)
w2_2 = GameSprite('platform2.png', 670, 100, 50, 400)
w2_3 = GameSprite('platform2.png', 670, 510, 50, 400)
w2_4 = GameSprite('platform2.png', 370, 510, 50, 400)
w2_5 = GameSprite('platform2.png', 900, 380, 50, 400)
w2_6 = GameSprite('platform2.png', 116, 300, 50, 400)
w2_7 = GameSprite('platform2.png', 116, 700, 50, 200)
barriers.add(w1)
barriers.add(w1_2)
barriers.add(w1_3)
barriers.add(w1_4)
barriers.add(w1_5)
barriers.add(w2)
barriers.add(w2_2)
barriers.add(w2_3)
barriers.add(w2_4)
barriers.add(w2_5)
barriers.add(w2_6)
barriers.add(w2_7)
packman = Player('hero.png', 250, 100, 80, 80, 0, 0)
monster = Player('cyborg.png', 1000,100,80,80,0, 0 )
run = True
while run:
    time.delay(50)
    window.fill(back)
    for e in event.get():
        if e.type == QUIT:
            run = False
        elif e.type == KEYDOWN:
            if e.key == K_LEFT:
                packman.x_speed = -5
                monster.x_speed = -5
            elif e.key == K_RIGHT:
                packman.x_speed = 5
                monster.x_speed = 5
            elif e.key == K_UP:
                packman.y_speed = -5
                monster.y_speed = -5
            elif e.key == K_DOWN:
                packman.y_speed = 5
                monster.y_speed = 5
            # elif e.key == K_a:
            #     monster.x_speed = -5
            # elif e.key == K_d:
            #     monster.x_speed = 5
            # elif e.key == K_w:
            #     monster.y_speed = -5
            # elif e.key == K_s:
            #     monster.y_speed = 5
        elif e.type == KEYUP:
            if e.key == K_LEFT:
                packman.x_speed = 0
                monster.x_speed = 0
            elif e.key == K_RIGHT:
                packman.x_speed = 0
                monster.x_speed = 0
            elif e.key == K_UP:
                packman.y_speed = 0
                monster.y_speed = 0
            elif e.key == K_DOWN:
                packman.y_speed = 0
                monster.y_speed  = 0
            # elif e.key == K_a:
            #     monster.x_speed = 0
            # elif e.key == K_d:
            #     monster.x_speed = 0
            # elif e.key == K_w:
            #     monster.y_speed = 0
            # elif e.key == K_s:
            #     monster.y_speed = 0    
            # elif e.key == K_a:
            #     monster.x_speed = 0
            # elif e.key == K_d:
            #     monster.x_speed = 0
            # elif e.key == K_w:
            #     monster.y_speed = 0
            # elif e.key == K_s:
            #     monster.y_speed = 0        
    # if finish == False:
    #     window.fill(back)
    #     barriers.draw(window)
        
    w1.reset()
    w1_2.reset()
    w1_3.reset()
    w1_4.reset()
    w1_5.reset() 
    w2.reset()
    w2_2.reset()
    w2_3.reset()
    w2_4.reset()
    w2_5.reset()
    w2_6.reset()
    w2_7.reset()
    packman.reset()
    packman.update()
    monster.reset()
    monster.update()
    display.update()