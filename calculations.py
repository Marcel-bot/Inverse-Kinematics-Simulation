from numpy import sqrt, sin, cos, arctan, arccos

a1 = 1
a2 = 1


def get_distance(origin: tuple[float, float, float], destination: tuple[float, float, float]) -> float:
    ox, oy, oz = origin
    px, py, pz = destination

    return sqrt((ox - px) ** 2 + (oy - py) ** 2 + (oz - pz) ** 2)


def get_d1(d: float) -> float:
    return (a1 ** 2 - a2 ** 2 + d ** 2) / (2 * d)


def get_radius(d1: float) -> float:
    return sqrt(a1 ** 2 - d1 ** 2)


def get_point_on_circle(r: float, alpha: float) -> tuple[float, float, float]:
    return r * cos(alpha), r * sin(alpha), 0


def get_sphere_intersection(
        origin: tuple[float, float, float],
        destination: tuple[float, float, float]
) -> tuple[float, float, float]:
    d = get_distance(origin, destination)
    d1 = get_d1(d)
    r = get_radius(d1)

    return d, d1, r


def get_intersection_center(
        origin: tuple[float, float, float],
        destination: tuple[float, float, float],
        d: float,
        d1: float
) -> tuple[float, float, float]:
    rap = d1 / d

    return (origin[0] - destination[0]) * rap, (origin[1] - destination[1]) * rap, (origin[2] - destination[2]) * rap


def get_a_respect_b(
        a: tuple[float, float, float],
        b: tuple[float, float, float],
        theta: float,
        phi: float
) -> tuple[float, float, float]:
    ax, ay, az = a
    bx, by, bz = b

    return (
        cos(theta) * cos(phi) * ax + sin(theta) * cos(phi) * ay - sin(phi) * az - bx,
        -sin(theta) * ax + cos(theta) * ay - by,
        cos(theta) * sin(phi) * ax + sin(theta) * sin(phi) * ay + cos(theta) * az - bz
    )


def get_polar_angles(point: tuple[float, float, float], radius: float) -> tuple[int, int]:
    return (
        arctan(point[1] / point[0]),
        arccos(point[2] / radius)
    )


def get_angles(
        origin: tuple[float, float, float],
        destination: tuple[float, float, float],
        alpha: float
) -> tuple[float, float, float, float]:
    d, d1, r = get_sphere_intersection(origin, destination)

    m = get_intersection_center(origin, destination, d, d1)

    w_m = get_point_on_circle(r, alpha)

    theta_m, phi_m = get_polar_angles(destination, d)

    w = get_a_respect_b(w_m, m, theta_m, phi_m)

    theta_1, phi_1 = get_polar_angles(w, a1)

    p_w = get_a_respect_b(destination, w, theta_1, phi_1)

    theta_2, phi_2 = get_polar_angles(p_w, a2)

    return theta_1, phi_1, theta_2, phi_2

