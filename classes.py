from abc import ABC, abstractmethod
import platform
import os
import sys

class GameControl():
    
    def __init__(self,game_height,game_width):
        self.game_height = game_height
        self.game_width = game_width
        self.world_map = []

    def world_gen(self):      
        for y in range(self.game_height):
            row = []
            for x in range(self.game_width):
                if y == 0 or y == self.game_height -1 or x == 0 or x == self.game_width -1:
                    row.append("@")
                else:
                    row.append(" ")
            self.world_map.append(row)
        return self.world_map

    def clear_move_cursor(self):
        sys.stdout.write("\033[H")
        sys.stdout.flush()
    
    def clear_screen():
        if platform.system() == "Windows":
            os.system("cls")
        else:
            os.system("clear")

    def render_world(self):
        for y in range(self.game_height):
            for x in range(self.game_width):
                print(self.world_map[y][x],end="")
            print()


class GameObject():
    def __init__(self,ypos,xpos):
        self.ypos = ypos
        self.xpos = xpos

    # All sub classes must have these methods...
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
    