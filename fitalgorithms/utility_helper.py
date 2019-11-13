import sys


def lb_to_kg(weight):
    return weight * 0.454


def kg_to_lb(weight):
    return weight / 0.454


def in_to_cm(height):
    if height is None:
        height = 0
    print(height)
    sys.stdout.flush()
    return height * 2.54


def cm_to_in(height):
    if height is None:
        height = 0
    return height / 2.54
