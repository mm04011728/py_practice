# coding:utf-8
from ground import ground
from egg import egg
from snake import snake


def main():
    game_ground = ground(20)
    game_snake = snake(game_ground)
    # empty_points = game_ground.get_empty_points()
    # for x, y in empty_points:
    #     print(x, y)
    game_egg = egg(game_ground)
    game_egg.refresh()
    # print(game_egg.position)

if __name__ == '__main__':
    main()
