import time


def can_move(i, u):
    iu = str(i) + str(u)
    if not iu.isdigit():
        return False
    return reduce(
        lambda x, y: int(x) + int(y),
        list(iu)
    )


def create_map_with_road(row_num=0, max_path=25, rows=20, cols=10):
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


def create_map_without_road(row_num=0, rows=20, cols=10):
    maps = []
    for i in xrange(1, rows + 1):
        maps.append([])
        for u in xrange(1, cols + 1):
            maps[row_num].append('-')
        row_num += 1
    return maps


def ant_dfs(maps, start=(10, 1), max_path=4, replace='*'):
    s = [start]
    start_x, start_y = start[0], start[1]
    visited = set()
    count = 0
    while s:
        x, y = s.pop()
        # if (x, y) not in visited and \
        #         can_move(x, y) <= max_path and \
        #         distance(start, (x, y)) <= max_path:
        if (x, y) not in visited and \
                can_move(x, y) <= max_path:
            maps[y][x] = replace
            count += 1
            # s += [(x+1, y), (x-1, y), (x, y+1), (x, y-1)]
            if can_move(x + 1, y):
                s.append((x + 1, y))
            if can_move(x - 1, y):
                s.append((x - 1, y))
            if can_move(x, y + 1):
                s.append((x, y + 1))
            if can_move(x, y - 1):
                s.append((x, y - 1))
            visited.add((x, y))
    print count


start_time = time.time()
maps = create_map_without_road(row_num=0, rows=2000, cols=2000)
ant_dfs(maps, start=(1000, 1000), max_path=25, replace='*')
print 'fill map without ant road:', time.time() - start_time

start_time = time.time()
maps = create_map_with_road(row_num=0, rows=2000, cols=2000)
ant_dfs(maps, start=(1000, 1000), max_path=25, replace='*')
print 'fill map with ant road:', time.time() - start_time
# 148848
