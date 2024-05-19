from calculations import get_angles
from numpy import pi

origin = (0, 0, 0)
dest = (1., 0, 0)


def inverse_kinematics(pos: tuple[int, int, int]):
    theta1, phi1, theta2, phi2 = 0, 0, 0, 0

    return theta1, phi1, theta2, phi2


def show():
    a1, a2, a3, a4 = get_angles(origin, dest, 0 * pi / 180)

    print(a1 * 180 / pi, a2 * 180 / pi, a3 * 180 / pi, a4 * 180 / pi)


if __name__ == '__main__':
    show()
