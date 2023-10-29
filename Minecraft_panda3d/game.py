from direct.showbase.ShowBase import ShowBase
from mapmanager import Mapmanager
from hero import Hero,Smiley
key_switch_mode = '/' 
class Game(ShowBase):
    def __init__(self):
        ShowBase.__init__(self)
        self.land = Mapmanager()
        self.switch_camera = 'sm'
        x,y = self.land.loadLand("land2.txt")
        self.hero = Hero((x//2,y//2,2),self.land)
        self.sm = Smiley((x//2.3,y//2.3,2),self.land)
        self.accept_mode()
        base.camLens.setFov(90)
    
    def accept_mode(self):
        base.accept(key_switch_mode, self.change_body)
    
    def change_body(self):
        if self.switch_camera == 'sm':
            self.switch_camera = 'ship'
        else:    
            self.switch_camera = 'sm'
game = Game()
game.run()