import math


def paraboloid(values, center, scale, max_value, vert_height=0):

    return scale * ((values[0] - center[0]) ** 2 + (values[1] - center[1]) ** 2) + vert_height



# FORMULA ----- f(x, y) = 1 / sqrt((x-h)^2 + (y-k)^2)
def metaball_function_2d(values, center, scale, max_value):

    try:
        height = scale / (((values[0] - center[0]) ** 2 + (values[1] - center[1]) ** 2) ** 0.5)
    except ZeroDivisionError:
        height = max_value

    if height > max_value:
        return max_value
    else:
        return height


# Base Function ---- f(x,y) = e^-(x^2 + y^2)
def normal_dist_3d(values, center, scale, max_value, size):

    height = scale * math.e ** - ((1/size) * ((values[0] - center[0])**2 + (values[1] - center[1])**2))

    if height > max_value:
        return max_value
    else:
        return height
