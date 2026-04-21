from abc import ABC, abstractmethod

class GameControl():
    pass

class GameObject():
    def __init__(self,ypos,xpos):
        self.ypos = ypos
        self.xpos = xpos

class Ball(GameObject):
    def collison():
        pass

class Charactor(ABC,GameObject):
    @abstractmethod
    def update_position():
        pass

class PlayerOne(Charactor):
    def update_position():
        pass

class PlayerTwo(Charactor):
    def update_position():
        pass
    