import time

def can_move(x, y, distance):
    xy = str(x) + str(y)
    if not xy.isdigit():
        return False
    return sum(map(int, xy)) <= distance


def create_map_with_road(row_num, max_path, rows, cols):
    count = 0
    maps = []
    for i in xrange(rows):
        maps.append([])
        for u in xrange(cols):
            if can_move(i, u) <= max_path:
                maps[row_num].append('+')
                count += 1
            else:
                maps[row_num].append('-')
        row_num += 1
    return maps


def create_map_without_road(row_num, rows, cols):
    maps = []
    for i in xrange(1, rows + 1):
        maps.append([])
        for u in xrange(1, cols + 1):
            maps[row_num].append('-')
        row_num += 1
    return maps


def ant_dfs(maps, start, max_path=4, replace='*'):
    s = [start]
    start_x, start_y = start[0], start[1]
    visited = set()
    count = 0
    while s:
        x, y = s.pop()
        if (x, y) not in visited and \
                can_move(x, y) <= max_path:
            maps[y][x] = replace
            count += 1
            if can_move(x + 1, y):
                s.append((x + 1, y))
            if can_move(x - 1, y):
                s.append((x - 1, y))
            if can_move(x, y + 1):
                s.append((x, y + 1))
            if can_move(x, y - 1):
                s.append((x, y - 1))
            visited.add((x, y))
    return count


start_time = time.time()
maps = create_map_without_road(row_num=0, rows=2000, cols=2000)
print ant_dfs(maps, start=(1000, 1000), max_path=25, replace='*')
print 'fill map without ant road:', time.time() - start_time

start_time = time.time()
maps = create_map_with_road(row_num=0, max_path=25, rows=2000, cols=2000)
print ant_dfs(maps, start=(1000, 1000), max_path=25, replace='*')
print 'fill map with ant road:', time.time() - start_time
# 148848
