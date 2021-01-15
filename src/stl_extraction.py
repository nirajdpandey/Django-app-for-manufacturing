import math
from math import sqrt


def calc_dimension(your_mesh):
    """
    Calculate dimension of the given mesh
        :return: dimension
        """
    minx = your_mesh.x.min()
    maxx = your_mesh.x.max()
    miny = your_mesh.y.min()
    maxy = your_mesh.y.max()
    minz = your_mesh.z.min()
    maxz = your_mesh.z.max()
    return minx, maxx, miny, maxy, minz, maxz


def len_width_hight(your_mesh):
    """
    calculate length, width and height of the mesh
    :return:
    """
    minx, maxx, miny, maxy, minz, maxz = calc_dimension(your_mesh)
    w1 = maxx - minx
    l1 = maxy - miny
    h1 = maxz - minz
    return w1, l1, h1


def circle_radius(a, b, c):
    # the sides cannot be negative
    if a < 0 or b < 0 or c < 0:
        return None
    else:
        # semi-perimeter of the circle
        p = (a + b + c) / 2

        # area of the traingle
        area = sqrt(p * (p - a) *
                    (p - b) * (p - c))
        # Radius of the incircle
        radius = area / p
        # Return the radius
    return radius


def sphere_surface_are(radius):
    sphere_surface = 4 * math.pi * radius * radius
    return sphere_surface
