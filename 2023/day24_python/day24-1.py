import sys

hailstones = [
    [[int(num) for num in part.split(", ")] for part in line.split(" @ ")]
    for line in open(sys.argv[1]).readlines()
]

POS_MIN = 200000000000000
POS_MAX = 400000000000000
# POS_MIN = 7
# POS_MAX = 27

NUM_INTERSECTIONS = 0

for i in range(len(hailstones)):
    for j in range(i + 1, len(hailstones)):
        hi = hailstones[i]
        hj = hailstones[j]
        # see whether lines hi and hj intersect between POS_MIN and POS_MAX (X/Y only)
        # (hi is [pos, dir])
        mi = hi[1][1] / hi[1][0]
        mj = hj[1][1] / hj[1][0]
        ci = hi[0][1] - hi[0][0] * mi
        cj = hj[0][1] - hj[0][0] * mj

        # ax+c=bx+d, x=(d-c)/(a-b)

        # print(mi, mj)
        if mi == mj:
            continue
        intersect_x = (cj - ci) / (mi - mj)
        intersect_y = mi * intersect_x + ci

        ti = (intersect_x - hi[0][0]) / hi[1][0]
        tj = (intersect_x - hj[0][0]) / hj[1][0]

        if ti < 0 or tj < 0:
            # collision happened in the past
            continue

        # print(intersect_x, intersect_y)

        if (
            intersect_x >= POS_MIN
            and intersect_x <= POS_MAX
            and intersect_y >= POS_MIN
            and intersect_y <= POS_MAX
        ):
            NUM_INTERSECTIONS += 1
            # print(f"Intersection {hi} {hj} at ({intersect_x:.3f}, {intersect_y:.3f})")
            # sys.exit(0)


# (intx,inty) = (x0,y0)+t*(x1,y1)
#  t=(intx-x0)/x1

print(f"Num intersections: {NUM_INTERSECTIONS}")
