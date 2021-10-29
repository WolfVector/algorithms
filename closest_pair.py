import math, copy

def closest_pair(Px, Py):
    if(len(Px) <= 3):
        return brute_force(Px, len(Px))

    half = int(len(Px) / 2)
    px_first_half = Px[:half]
    px_second_half = Px[half:]

    middle = Px[half]
    py_first_half = py_left_sort(Py, middle)
    py_second_half = py_right_sort(Py, middle)

    pl, dl = closest_pair(px_first_half, py_first_half)
    pr, dr = closest_pair(px_second_half, py_second_half)

    best = min(dl, dr)

    ps, ds = split_pair(Py, Px[half - 1], best)

    best = ds
    p = ps

    if(dl < dr and dl < ds):
        best = dl
        p = pl
    elif(dr < dl and dr < ds):
        best = dr
        p = pr

    return (p, best)

def brute_force(P, size):
    min_val = float('inf')
    p = (P[0], Point(0, 0))
    for i in range(size):
        for j in range(i + 1, size):
            dist = dist_point(P, i, j)
            if(dist < min_val):
                min_val = dist
                p = (P[i], P[j])

    return (p, min_val)

def dist_point(P, i, j):
    return math.sqrt((P[i].x - P[j].x)**2 + (P[i].y - P[j].y)**2)

def py_left_sort(Py, middle):
    array = []
    for p in Py:
        if(p.x < middle.x):
            array.append(p)

    return array

def py_right_sort(Py, middle):
    array = []
    for p in Py:
        if(p.x >= middle.x):
            array.append(p)

    return array

def split_pair(Py, x, best):
    sy = []
    for p in Py:
        if(abs(p.x - x.x) < best):
            sy.append(p)

    size = min(8, len(sy))
    print(size)
    return brute_force(sy, size)

class Point():
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return "("+ str(self.x) + ", " + str(self.y) + ")"

Px = [Point(2, 3), Point(12, 30),
     Point(40, 50), Point(5, 1),
     Point(12, 10), Point(3, 4)]

Px.sort(key = lambda point: point.x)
Py = copy.deepcopy(Px)
Py.sort(key = lambda point: point.y)

p, d = closest_pair(Px, Py)
print(p[0], p[1])
print(d)
