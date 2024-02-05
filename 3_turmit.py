class TapeLetter:
    L = 'L'
    R = 'R'
    # U = 'U'
    # D = 'D'
    S = 'S'
    F = 'F'
    M = 'M'
    s = 'a'

    def __init__(self):
        pass


class Direction:
    UP = 'UP'
    DOWN = 'DOWN'
    LEFT = 'LEFT'
    RIGHT = 'RIGHT'
    LEFT_UPPER = 'LEFT_UPPER'
    LEFT_LOWER = 'LEFT_LOWER'
    RIGHT_UPPER = 'RIGHT_UPPER'
    RIGHT_LOWER = 'RIGHT_LOWER'

    def get_direction(self):
        if self.direction_word == Direction.UP:
            return 90
        if self.direction_word == Direction.DOWN:
            return 270
        if self.direction_word == Direction.LEFT:
            return 180
        if self.direction_word == Direction.RIGHT:
            return 0

    def rotate_left(self):
        if self.direction != Direction.DOWN:
            self.direction += 90
        else:
            self.direction = 0

    def rotate_right(self):
        if self.direction != Direction.RIGHT:
            self.direction -= 90
        else:
            self.direction = 270

    def __init__(self):
        self.direction_word = Direction.RIGHT
        self.direction = 0


tape = [
    TapeLetter.L,
    TapeLetter.L,
    TapeLetter.M,
    TapeLetter.R,
    TapeLetter.L,
    TapeLetter.L,
    TapeLetter.s,
]


class Object2D(object):
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.direction = Direction.UP

    def move_left(self):
        self.x -= 1

    def move_right(self):
        self.x += 1

    def move_up(self):
        self.y += 1

    def move_down(self):
        self.y -= 1


class Ant(Object2D):
    def __init__(self, x, y):
        super(Ant, self).__init__(x, y)


field = [[]]


def read_tape(tape_arg, ant_obj):
    position = 0
    for _ in xrange(25):
        print \
            'TapeLetter:', \
            tape_arg[position], \
            ', ant.position:', \
            ant_obj.x, ant_obj.y, \
            ', tape.position:', \
            position

        if tape_arg[position] == TapeLetter.s:
            position = 0
        elif tape_arg[position] == TapeLetter.L:
            ant_obj.move_left()
        elif tape_arg[position] == TapeLetter.R:
            ant_obj.move_right()
        # elif tape_arg[position] == TapeLetter.U:
        #     ant_obj.move_up()
        # elif tape_arg[position] == TapeLetter.D:
        #     ant_obj.move_down()
        else:
            raise Exception('Such Letter: "', tape_arg[position], '" at position', position, 'of Tape doesn\'t exist')

        position += 1
        if position >= len(tape_arg):
            raise Exception('Tape length lesser than:', position)


# ant = Ant(10, 10)
# read_tape(tape, ant)
direction = Direction()
for _ in range(5):
    direction.rotate_left()
    print(direction.get_direction())
