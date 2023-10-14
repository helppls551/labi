
key_switch_camera = 'c'
key_switch_mode = 'z'

key_forward = 'w'
key_back ='s'
key_left = 'a'
key_right = 'd'
key_up = 'e'
key_down = 'q'

key_turn_left = 'n'
key_turn_right = 'm'

class Hero():
    def __init__(Self,pos,land):
        self.land = land
        self.mode = True #режим прохождения сквозь всё
        self.hero = loader.loadModel('smiley')
        self.hero.setColor(1,0.5,0)
        self.hero.setSclae(0.3)
        self.hero.reparentTo(render)
        self.cameraBind()
        self.accept_events()
    
    def cameraBind(self):
        base.disableMouse()
        base.camera.setH(180)
        base.camera.reparentTo(self.hero)
        base.camerPos(0,0,1.5)
        self.cameraOn = True

    def cameraUp(self):
        pos = self.hero.getPos()
        base.mouseInterfaceNode.SetPos(-pos[0],-pos[1],-pos[2]-3)
        base.camera.reparentTo
        base.enableMouse()
        self.cameraOn = False

    def changeView(self):
        if self.cameraOn:
            self.cameraUp()
        else:
            self.cameraBind()

    def turn_right