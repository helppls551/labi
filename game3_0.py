from direct.showbase.ShowBase import ShowBase

from mapmanage2_0 import Mapmanager

class Game(ShowBase):
    def __init__(self):
        ShowBase.__init__(self)
        self.land = Mapmanager()
        filename = 'lan2.txt'
        self.land.loadLand(filename)
        base.camLens.setFov(90)

game = Game()
game.run()