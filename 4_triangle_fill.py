def ant_can_move(x, y, rule):
    return sum(map(int, str(x) + str(y))) <= rule


def ant_field(x, y, rule):
    stack = [(x, y)]
    visited = set()
    count = 0
    while stack:
        x, y = stack.pop()
        if (x + 1, y) not in visited and ant_can_move(x + 1, y, rule):
            stack.append((x + 1, y))
        if (x, y + 1) not in visited and ant_can_move(x, y + 1, rule):
            stack.append((x, y + 1))
        visited.add((x, y))
        count += 1
    return count


print ant_field(1000, 1000, 25)
