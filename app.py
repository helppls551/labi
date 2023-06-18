import pygame

window = pygame.display.set_mode((700,500))
pygame.display.set_caption('Fastcliccer')
window.fill((255,255,255))
game = True
class area():
    def __init__(self,x,y,width,height,color):
        self.x = x
        self.y = y
        self.rect = pygame.Rect(self.x,self.y,width,height)
        self.color = color
    def fill(self):
        pygame.draw.rect(window,self.color,self.rect)
    def img(self):
        pygame.draw.rect('sans.png')
        # back = pygame.image.load('sans.png')
        # back = pygame.transform.scale(back,self.rect.width,self.rect.height)
card_1 = area(350,250,100,100,(255,255,255))
card_1.fill()
card_1.img()
while game:
    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            game = False

    pygame.display.update()
    pygame.time.delay(25)