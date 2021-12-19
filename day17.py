def hits_target(minx, maxx, loy, hiy, x_velocity, y_velocity) -> int:
    x = 0
    y = 0
    maxy = 0
    while True:
        x += x_velocity
        y += y_velocity

        maxy = max(maxy, y)
        if minx <= x <= maxx and loy <= y <= hiy:
            return maxy
        elif y < loy or x > maxx:
            return -1

        if x_velocity > 0:
            x_velocity -=1
        elif x_velocity < 0:
            x_velocity += 1
        y_velocity -= 1
    return -1


def part1():
    # Test input
    # minx, maxx = 20, 30
    # loy, hiy = -10, -5

    # Puzzle input
    minx, maxx = 230, 283
    loy, hiy = -107, -57
    # x_velocity, y_velocity = 6,9

    maxy = 0
    for x_velocity in range(1, maxx):
        for y_velocity in range(1, 1000):
            y = hits_target(minx, maxx, loy, hiy, x_velocity, y_velocity)
            if y > maxy:
                maxy = y

    print(f"{maxy=}")
    return


def part2():
    # Test input
    # minx, maxx = 20, 30
    # loy, hiy = -10, -5

    # Puzzle input
    minx, maxx = 230, 283
    loy, hiy = -107, -57

    count = 0
    for x_velocity in range(1, maxx+1):
        for y_velocity in range(loy, 1000):
            y = hits_target(minx, maxx, loy, hiy, x_velocity, y_velocity)
            if y > -1:
                #print(f"{x_velocity},{y_velocity}")
                count += 1

    print(f"{count=}")
    return


def main():
    #part1()
    part2()


if __name__ == "__main__":
    main()
