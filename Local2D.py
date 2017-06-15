# Monte Carlo Localization of a robot in a 2 dimensional cyclic world


def localization(world, motions, measurements, sensor_right, p_move):
    pinit = 1.0 / float(len(world)) / float(len(world[0]))  # Initial uniform distribution
    p = [[pinit for col in range(len(world[0]))] for row in range(len(world))]

    for i in range(len(measurements)):
        p = move(p, motions[i], p_move)
        p = sense(p, measurements[i], world, sensor_right)

    return p


# Determines the current position of the robot in the world
def sense(p, Z, world, sensor_right):
    q = [[] for _ in range(len(p))]

    for row in range(len(world)):
        for col in range(len(world[0])):
            hit = (world[row][col] == Z)  # Check whether measurement matches the colour of the cell in the world
            q[row].append(p[row][col] * (hit * sensor_right + (1 - hit) * (1 - sensor_right)))

    qsum = sum(map(sum, q))

    for row in range(len(q)):
        for col in range(len(q[0])):
            q[row][col] /= qsum

    return q


# Move: [0, 0]- no motion, [0, 1]- move right, [0. -1]- move left, [1, 0]- move down, [-1, 0]- move up
def move(p, U, p_move):
    q = [[] for _ in range(len(p))]

    for row in range(len(p)):
        for col in range(len(p[0])):
            q[row].append(p_move * p[(row - U[0]) % len(p)][(col - U[1]) % len(p[0])] + (1 - p_move) * p[row][col])

    return q


def show(p):
    rows = ['[' + ', '.join(map(lambda x: '{0:.5f}'.format(x), r)) + ']' for r in p]
    print('[' + ',\n '.join(rows) + ']')


if __name__ == '__main__':
    world = [['r', 'g'], ['r', 'r'], ['g', 'r'], ['r', 'g'], ['g', 'g']]
    motions = [[0, 0], [-1, 0], [0, 1], [0, -1], [0, 1], [1, 0]]
    measurements = ['r', 'r', 'g', 'g', 'g', 'r']
    sensor_right = 0.99  # probability that the sensor measurement is correct
    p_move = 0.97  # probability that the motion is executed correctly.
    p = localization(world, motions, measurements, sensor_right, p_move)

    show(p)
