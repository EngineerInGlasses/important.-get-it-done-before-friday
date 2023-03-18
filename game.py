# x^-2+y^-2=1^-2
from direct.showbase.ShowBase import ShowBase 
from mapmanager import Mapmanager
from hero import Hero
class Game (ShowBase):
    def __init__(self):
        ShowBase.__init__(self)
        self.land = Mapmanager()
        self.land.loadLand('land.txt')
        meself = Hero((20, 10, 20), self.land)
        base.camLens.setFov(110)
moya_igra = Game()
moya_igra.run()