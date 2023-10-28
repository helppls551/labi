from direct.showbase.ShowBase import ShowBase

from mapmanage3_0 import Mapmanager
from hero import Hero

class Game(ShowBase):
    def __init__(self):
        ShowBase.__init__(self)
        self.land = Mapmanager()
        x, y =self.land.loadLand('lan2.txt')
        self.hero = Hero(pos(x//2,y//2,2),self.land)
        base.camLens.setFov(90)

game = Game()
game.run()