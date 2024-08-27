#作者：Alex
#2024 / 8 / 26
#上午12: 20

black_point = {(6, 6), (3, 3), (4, 5)}
result = True
for x in range(8):
    if not result:
        break
    for y in range(8):
        if not result:
            break
        a = (x, y)
        neighbor_count = 0
        if a in black_point:
            for dx in range(-1, 2):
                for dy in range(-1, 2):
                    neighbor = (x+dx, y+dy)
                    if 0 <= neighbor[0] < 8 and 0 <= neighbor[1] < 8:
                        if neighbor == a:
                            continue
                        if neighbor in black_point:
                            neighbor_count += 1
            if neighbor_count != 2:
                result = False


if not result:
    print('该图形不为0')
else:
    print('该图形为0')

