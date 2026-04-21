from classes import GameControl

def main():
    game_control = GameControl(25,90)

    game_control.world_gen()
    game_control.render_world()

#Program Entry Point
if __name__ == "__main__":
    main()