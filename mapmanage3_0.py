class Mapmanager():
    def __init__(self):
        self.model = 'block.egg'
        self.texture = 'blcok.png'
        self.colors=[
            (0.2,0.2,0.35,1),
            (0.2,0.5,0.2,1),
            (0.7,0.2,0.2,1),
            (0.5,0.3,0.0,1)
        ]
        self.startNew()

    def startNew(self):
        self.land = render.attachNewNode('Land')
    
    def getColor(self,2):
        return self.colors[z%4]
    
    def addBlock(self,position):
        self.block = loader.loadModel(self.model)
        self.block.setTexture(loader.loadTexture self.texture)
        self.block.setPos(position)
        self.color = self.getColor(int.position[2])