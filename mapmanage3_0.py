class Mapmanager():
    def __init__(self):
        self.model = 'block'
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
    
    def getColor(self,z):
        if z <len(self.colors):
            return self.color[z]
        else:
            return self.colors[len(self.colors)-1]
    
    
    def addBlock(self,position):
        self.block = loader.loadModel(self.model)
        self.texture = self.textures[text]
        self.block.setTexture(loader.loadTexture(self.texture))
        self.block.setPos(position)
        self.color = self.getColor(int.position[2])
        self.block.setColor(self.color)
        self.block.setTag('at',str(position))
        self.block.reparentTo(self.land)


    def clear(self):
        self.land.removeNode()
        self.startNew()
    
    def loadLand(self,filename):
        self.clear()
        with open(filename) as file:
            y = 0
            for line in file:
                x = 0
                line = line.split(' ')
                for z in line:
                    for z0 in range(int(z)+1):
                        block = self.addBlock((x,y,z0))
                    x+= 1
                y+=1
        return x,y
    
    def findBlocks(self,pos):
        return self.land.findAllMatches('=at=' + str(pos))
    
    def isEmpty(self,pos):
        blocks = self.findBlocks(pos)
        if blocks:
            return False
        else:
            True
    
    def findHighestEmpty(self,pos):
        x,y,z =pos
        z = 1
        while not self.isEmpty((x,y,z)):
            z+= 1
        return(x,y,z)
    
    def buildBlock(self,pos,text = 0):
        x,y,z = pos
        new = self.findHighestEmpty(pos)
        if new[2] <= z+1:
            self.addBlock(new,text)
    
    def delBlock(self,position):
        x,y,z = self.findHighestEmpty(position)
        pos = x,y,z-1
        for block in self.findBlocks(pos):
                block.removeNode()
    
    def saveMap(self):
        blocks = self.land.getChildren()
        with open('my_map.dat','wb') as fout:
            pickle.dump(len(blocks),fout)
        for block in blocks:
            x,y,z =  block.getPos()
            pos = (int(x),int(y),int(z))
            pickle.dump(pos,fout)
            if 'wood.png' in str(block.getTexture()):
                pickle.dump(object:1,fout)
            else:
                pickle.dump(object:1,fout)
    
    def loadMap(self):
        self.clear()
        with open('my_map_dat','rb') as fin:
            length = pickle.load(fin)
            for i in range(length):
                pos = pickle.load(fin)
                text = pickle.load(fin)
                self.addBlock(pos,text)
