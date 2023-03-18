from direct.showbase.ShowBase import ShowBase 
from mapmanager import Mapmanager
from dummy import Hero
class Game (ShowBase):
    def __init__(self):
        ShowBase.__init__(self)
        self.land = Mapmanager()
        self.land.loadLand('land.txt')
        meself = Hero((5, 15, 2), self.land)
        base.camLens.setFov(110)
moya_igra = Game()
moya_igra.run()