from collections import namedtuple

Point = namedtuple('Point', ['x', 'y'])


def ant_can_move(x, y, distance):
    num = str(x) + str(y)
    if not num.isdigit():
        return False
    return sum(map(int, str(x) + str(y))) <= distance


def ant_dfs(x, y, distance):
    s = [(x, y)]
    visited = set()
    count = 0
    while s:
        x, y = s.pop()
        if ant_can_move(x, y, distance) and (x, y) not in visited:
            s.append((x - 1, y))
            s.append((x + 1, y))
            s.append((x, y + 1))
            s.append((x, y - 1))
            visited.add((x, y))
            count += 1
    return count


ant_dfs(100000, 100000, 25)
# 148848
