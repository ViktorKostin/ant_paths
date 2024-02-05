from collections import namedtuple

Point = namedtuple('Point', ['x', 'y'])


def ant_can_move(point, distance):
    num = str(point.x) + str(point.y)
    if not num.isdigit():
        return False
    return reduce(
        lambda x, y: int(x) + int(y),
        list(num)
    ) <= distance


def ant_dfs(start=Point(10, 2), distance=3):
    s = [start]
    visited = set()
    count = 0
    while s:
        point = s.pop()
        if ant_can_move(point, distance) and point not in visited:
            s.append(Point(point.x - 1, point.y))
            s.append(Point(point.x + 1, point.y))
            s.append(Point(point.x, point.y + 1))
            s.append(Point(point.x, point.y - 1))
            visited.add(point)
            count += 1
    return count


ant_dfs(start=Point(100000, 100000), distance=25)
# 148848
