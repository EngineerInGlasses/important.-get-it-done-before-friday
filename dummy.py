class Hero():
    def __init__(self, pos, land):
        self.mode = True
        self.land = land # Подготавливаем 'папочку'
        self.hero = loader.loadModel('smiley') # Придаём форму
        self.cameraBind()           # Закрепляем камеру на игроке
        self.hero.setColor(1, 0.5, 0.5)   # Устанавливаем цвет
        self.hero.setScale(0.5)     # Устанавливаем размеры
        self.hero.setPos(pos)       # Устанавливаем позицию
        self.accept_events()        # Подписываемся на все события
        self.hero.reparentTo(render)  # Отправляем к 'папочке' (типа reparent, parent - родитель)
#
    def cameraBind(self):
        base.disableMouse()         # Отключаем мышь
        base.camera.setH(180)       # Разворачиваем на 180
        base.camera.setPos(0, 0, 1.5)       # Устанавливаем позицию (внутри игрока)
        self.cameraOn = True
        base.camera.reparentTo(self.hero)   # Отправляем игроку
#
    def cameraUp(self):
        pos = self.hero.getPos()    # Получаем координаты игрока
        base.mouseInterfaceNode.setPos(-pos[0], -pos[1], -pos[2] - 3)   # даём камере взмыть над игроком
        base.enableMouse()          # Включаем мышь
        self.cameraOn = False
        base.camera.reparentTo(render)  # Отправляем к 'папочке'
#
    def accept_events(self):
        base.accept('c', self.changeMode)
        base.accept('v', self.turn_left)
        base.accept('v' + '-repeat', self.turn_left)
        base.accept('b', self.turn_right)
        base.accept('b' + '-repeat', self.turn_right)
        base.accept('w' + '-repeat', self.forward)
        base.accept('w', self.forward)
        base.accept('a' + '-repeat', self.left)
        base.accept('a', self.left)
        base.accept('s' + '-repeat', self.back)
        base.accept('s', self.back)
        base.accept('d' + '-repeat', self.right)
        base.accept('d', self.right)
#
    def changeMode(self):
        if self.cameraOn == True:
            self.cameraUp()
        elif self.cameraOn == False:
            self.cameraBind()
        self.mode = not self.mode
#
    def turn_left(self):
        self.hero.setH((self.hero.getH() + 5) % 360)
#
    def turn_right(self):
        self.hero.setH((self.hero.getH() - 5) % 360)
#
    def move_to(self, angle):
        if self.mode:
            self.just_move(angle)
        elif not self.mode:
            self.try_move(angle)
#
    def try_move(self, angle):
        pass
#
    def just_move(self, angle):
        pos = self.look_at(angle)
        self.hero.setPos(pos)
#
    def check_dir(self, angle):
        if angle >= 0 and angle < 20:
            return 0, -1
        elif angle >= 20 and angle < 65:
            return 1, -1
        elif angle >= 65 and angle < 110:
            return 1, 0
        elif angle >= 110 and angle < 155:
            return 1, 1
        elif angle >= 155 and angle < 200:
            return 0, 1
        elif angle >= 200 and angle < 245:
            return -1, 1
        elif angle >= 245 and angle < 300:
            return -1, 0
        elif angle >= 300 and angle < 345:
            return -1, -1
        else:
            return 0, -1
#
    def look_at(self, angle):
        from_z = round(self.hero.getZ())
        from_y = round(self.hero.getY())
        from_x = round(self.hero.getX())
        dx, dy = self.hero.check_dir(self, angle)
        return from_x + dx, from_y + dy, from_z
#
    def forward(self):
        angle = self.hero.getH()
        self.move_to(angle)
#
    def left(self):
        angle = (self.hero.getH() + 90) % 360
        self.move_to(angle)
#
    def back(self):
        angle = (self.hero.getH() + 180) % 360
        self.move_to(angle)
#
    def right(self):
        angle = (self.hero.getH() + 270) % 360
        self.move_to(angle)