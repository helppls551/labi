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

class Bullet(GameSprite):
    def __init__(self, player_image, player_x, player_y, size_x, size_y,player_speed):
        super().__init__(player_image, player_x, player_y, size_x, size_y)
        self.speed = player_speed
    def update(self):
        self.rect.x += self.speed
        if self.rect.x > win_width + 10:
            self.kill()

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
    def fire(self):
        bullet = Bullet('bullet.png',self.rect.centerx,self.rect.top,30,35,15)
        bullets.add(bullet)

class Enemy(GameSprite):

    def __init__(self,player_image,player_x,player_y,size_x,size_y,player_speed_x):
        GameSprite.__init__(self,player_image ,player_x,player_y,size_x,size_y)
        self.speed_x = player_speed_x
        
        self.side_x = 'left'
        self.side_y = 'up'
    
    def collide_x(self,mob):
        if mob.rect.right > self.rect.left and \
        mob.rect.left < self.rect.right:
            return True
    def collide_y(self,mob):
        if mob.rect.bottom > self.rect.top and \
        mob.rect.top < self.rect.bottom:
            return True
    
    def update(self):
        plat_tuched = sprite.spritecollide(self,barriers,False)
        if plat_tuched and self.side_x == 'left':
            self.side_x = 'right'
        elif plat_tuched and self.side_x == 'right':
            self.side_x = 'left'
        if  plat_tuched and self.side_y == 'up':
            self.side_y = 'down'
        elif plat_tuched and self.side_y == 'down':
            self.side_y = 'up'
        if self.side_x == 'left':
            self.rect.x += -5
        elif self.side_x == 'right':
            self.rect.x +=5
        if self.side_y == 'up':
            self.rect.y += -5
        elif self.side_y == 'down':
            self.rect.y += 5
win_width = 1240
win_height = 840
window = display.set_mode((win_width, win_height))
display.set_caption("Лабиринт")
back = (119, 210, 223)
barriers = sprite.Group()
bullets = sprite.Group()
monsters = sprite.Group()
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
wall_w = GameSprite('platform1.png', 0,0,win_width,1)
wall__w = GameSprite('platform1.png',win_width,0,win_width,1)
wall_h = GameSprite('platform2.png',0,0,1,win_height)
wall__h = GameSprite('platform2.png',win_width,0,1,win_height)
win_bar = GameSprite('pac-1.png',500,500,80,80)
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
barriers.add(wall_h)
barriers.add(wall__h)
barriers.add(wall_w)
barriers.add(wall__w)

packman = Player('hero.png', 250, 100, 80, 80, 0, 0)
monster = Enemy('cyborg.png', 1000,100,80,80,0)
monsters.add(monster)
run = True
finish = True
while run:
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
            elif e.key == K_SPACE:
                packman.fire()
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
                monster.y_speed = 0
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
        
    # w1.reset()
    # w1_2.reset()
    # w1_3.reset()
    # w1_4.reset()
    # w1_5.reset() 
    # w2.reset()
    # w2_2.reset()
    # w2_3.reset()
    # w2_4.reset()
    # w2_5.reset()
    # w2_6.reset()
    # w2_7.reset()
    if finish:
        window.fill(back)
        barriers.draw(window)
        win_bar.reset()
        packman.reset()
        packman.update()
        bullets.update()
        bullets.draw(window)
        sprite.groupcollide(bullets,barriers,True,False)
        if sprite.spritecollide(packman,monsters,True):
            finish = False
            img = image.load('game-over_1.png')
            window.fill((255,255,255))
            window.blit(transform.scale(img,(win_width,win_height)),(0,0))
        if not(sprite.groupcollide(monsters,bullets,True,True)):
            monsters.draw(window)
            monster.update()
        if sprite.collide_rect(packman,win_bar):
            finish = False
            img = image.load('thumb.jpg')
            window.fill((255,255,255))
            window.blit(transform.scale(img,(win_width,win_height)),(0,0))
        if sprite.spritecollide(win_bar,monsters,True):
            finish = False
            img = image.load('thumb.jpg')
            window.fill((255,255,255))
            window.blit(transform.scale(img,(win_width,win_height)),(0,0))    
    time.delay(25)
    display.update()