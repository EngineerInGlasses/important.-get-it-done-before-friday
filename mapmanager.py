# напиши здесь код создания и управления картой
class Mapmanager():
    def __init__(self):
        self.model = 'block.egg'
        self.texture = "block.png"
        self.colors = [(0.1, 0.5, 0.4, 0),
                      (0.2, 0.4, 0.1, 0),
                      (0.3, 0.3, 0.3, 0),
                      (0.5, 0.7, 0, 0)]
        self.startNew()
    def addBlock(self, position):
        self.block = loader.loadModel(self.model)
        self.block.setTexture(loader.loadTexture(self.texture))
        self.block.setPos(position)
        self.color = self.getColor(position[2])
        self.block.setColor(self.color)
    def getColor (self, z):
        if z < len(self.colors):
            return self.colors[z]
        else:
            return self.colors[2]
    def startNew (self):
        self.land = render.attachNewNode("Land")
    def color_change(self):
        self.color[0] += 0.5
        self.color[1] += 0.5
        self.color[2] += 0.5
        self.color[3] += 0.5
    def loadLand(self, filename):
        with open(filename, 'r') as le_land:
            y = 0
            lines = le_land.readlines()
            for l in lines:
                x = 0
                l = map(int, l.split(' '))
                for n in l:
                    for z in range(-1, n):
                        self.addBlock((x, 5+y, z))
                        self.block.reparentTo(self.land)
                    x += 1
                y += 1