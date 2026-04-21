from abc import ABC, abstractmethod

class GameControl():
    def world_gen():
        pass

    def render_world():
        pass


class GameObject():
    def __init__(self,ypos,xpos):
        self.ypos = ypos
        self.xpos = xpos
    @abstractmethod
    def update_position():
        pass

class Ball(GameObject):
    def update_position():
        pass

class PlayerOne(GameObject):
    def update_position():
        pass

class PlayerTwo(GameObject):
    def update_position():
        pass
    