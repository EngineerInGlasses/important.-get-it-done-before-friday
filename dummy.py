class Hero():
    def __init__(self, pos, land):
        self.land = land # Подготавливаем 'папочку'
        self.hero = loader.loadModel('smiley') # Придаём форму
        self.cameraBind()           # Закрепляем камеру на игроке
        self.hero.setColor(1, 0.5, 0.5, )   # Устанавливаем цвет
        self.hero.setScale(0.5)     # Устанавливаем размеры
        self.hero.setPos(pos)       # Устанавливаем позицию
        self.accept_events()        # Подписываемся на все события
        self.hero.reparentTo(render)  # Отправляем к 'папочке' (типа reparent, parent - родитель)
'''~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~'''
    def cameraBind(self):
        base.disableMouse()         # Отключаем мышь
        base.camera.setH(180)       # Разворачиваем на 180
        base.camera.reparentTo(self.hero)   # Отправляем игроку
        base.camera.setPos(0, 0, 1.5)       # Устанавливаем позицию (внутри игрока)
        self.cameraOn = True
'''~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~'''
    def cameraUp(self):
        pos = self.hero.getPos()    # Получаем координаты игрока
        base.mouseInterfaceNode.setPos(-pos[0], -pos[1], -pos[2] - 3)   # даём камере взмыть над игроком
        base.camera.reparentTo(render)  # Отправляем к 'папочке'
        base.enableMouse()          # Включаем мышь
        self.cameraOn = False
'''~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~'''
    def accept_events(self):
        base.accept('c', self.changeView)    # кнопка для смены вида (пока не работает)
        base.accept('v', self.turn_left)                # \
                                                        #  > кнопка для поворота камеры влево (пока не работает)
        base.accept('v' + '-repeat', self.turn_right)   # /
        base.accept('b', self.turn_left)                # \
                                                        #  > кнопка для поворота камеры вправо (пока не работает)
        base.accept('b' + '-repeat', self.turn_right)   # /
'''~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~'''
    def changeView(self):
        if self.cameraOn == True:
            self.cameraUp()
        elif self.cameraOn == False:
            self.cameraBind()
'''~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~'''
    def turn_left(self):
        self.hero.setH((self.hero.getH() + 5) % 360)
'''~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~'''
    def turn_right(self):
        self.hero.setH((self.hero.getH() - 5) % 360)
    def 