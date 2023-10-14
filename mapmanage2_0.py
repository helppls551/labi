class Mapmanager():
    def __init__(self):
        self.model = 'block.egg'
        self.texture = 'block.png'
        self.colors = [
            (0.2,0.2,0.35,1),
            (0.2,0.5,0.2,1),
            (0.7,0.5,0.2,1),
            (0.5,0.3,0.0,1)
        ]

        self.startNew()

    def startNew(self):
        self.land = render.attachNewNode('Land')

    def getColor(self,z):
        return self.colors[z%4]
    
    def addBlock(self, position):
        self.block = loader.loadModel(self.model)
        self.block.setTexture(loader.loadTexture(self.texture))
        self.block.setPos(position)
        self.color = self.getColor(int(position[2]))
        self.block.setColor(self.color)
        self.block.reparentTo(self.land)

    def clear(self):
        self.land.removeNode()
        self.startNew()

    def pot(self,x,y,z):
        self.clear()
        self.addBlock((x,y,0))
        self.addBlock((x,y,z))

    def loadLand(self, filename):
        self.clear()
        with open(filename) as file:
            y = 0
            for line in file:
                x = 0
                line = line.split()
                for z in line:
                    for z0 in range(int(z)+1):
                        if z == ' ':
                            self.pot(x,y,abs(z0))
                        else:
                            self.addBlock((x,y,z0))    
                    x += 1
                y += 1 