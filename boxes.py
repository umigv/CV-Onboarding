import time

# fmt: off
start_txt = \
"""\
xxxxxxxxxxxx
x~~....~~~~x
x~..~~....~x
x~~...~~~..x
x~~.....~~.x
x.s.~~~~~..x
x~~~~~.....x
x~~.......~x
x.....~~~~~x
x.@.~~~~~~~x
x~~~~~..e..x
xxxxxxxxxxxx
"""
# fmt: on


w = 12
h = 12

c_player = "@"
c_wall = "x"
c_air = "."
c_lava = "~"
c_switch = "s"
c_exit = "e"


def add(a: tuple[int, int], b: tuple[int, int]):
    return (a[0] + b[0], a[1] + b[1])


class Game:
    def __init__(self, level: str):
        self.static = level
        self.player_pos = self.get_pos(c_player)
        self.switch_pos = self.get_pos(c_switch)
        self.exit_pos = self.get_pos(c_exit, False)
        # print(self.player_pos[0], self.player_pos[1])
        # print(self.static)

        self.loop()

    # returns zero indexed positions
    def get_pos(self, c: str, delete: bool = True):
        pos = 0
        for i in range(0, h * (w + 1)):
            if self.static[i] == c:
                pos = i
                if delete:
                    self.static = self.static.replace(c, c_air)
            # print(self.static[i], end="")

        # print(pos)
        x = pos // (w + 1)
        y = pos % (w + 1)
        return (x, y)

    def to_index(pos: tuple[int, int]):
        return pos[0] * (w + 1) + pos[1]

    def display(self):
        for i in range(0, h * (w + 1)):
            if Game.to_index(self.player_pos) == i:
                print(c_player, end="")
            else:
                print(self.static[i], end="")

    def loop(self):
        alive = True
        while alive:
            self.display()
            direction = input("Direction: ")
            attempt = (0, 0)
            dict = {"a": (0, -1), "d": (0, 1), "w": (-1, 0), "s": (1, 0)}
            if dict.__contains__(direction):
                attempt = dict[direction]

            new = add(self.player_pos, attempt)
            print(new)

            match (self.static[Game.to_index(new)]):
                case "x":
                    pass
                case "~":
                    alive = False
                    break
                case "e":
                    break
                case _:
                    self.player_pos = new

            if self.player_pos == self.switch_pos:
                print("switch activated. lava drained.")
                self.static = self.static.replace("~", ".")
                time.sleep(1)
        if alive:
            print("you win. wow. you have so much patience.")
        else:
            print("you died. lol. rip.")


if __name__ == "__main__":
    print("wasd to move. find the hidden switch to unlock the exit. [~] will kill you")
    game = Game(start_txt)
