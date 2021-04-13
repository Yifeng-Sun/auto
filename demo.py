from Mapnode import *
from Hdmap import *

# 初始化基准HDMap
GTHD = Hdmap(14, 11)

GTHD.set(1, 2, "restaurant")
GTHD.set(1, 3, "restaurant")
GTHD.set(1, 4, "restaurant")
GTHD.set(2, 2, "restaurant")
GTHD.set(2, 3, "restaurant")
GTHD.set(2, 4, "restaurant")
GTHD.set(3, 2, "restaurant")
GTHD.set(3, 3, "restaurant")
GTHD.set(3, 4, "restaurant")

GTHD.set(5, 3, "store")
GTHD.set(5, 4, "store")
GTHD.set(6, 3, "store")
GTHD.set(6, 4, "store")

for x in range(1, 7):
    for y in range(6, 10):
        GTHD.set(x, y, "hospital")

GTHD.set(8, 8, "tree")
GTHD.set(9, 8, "tree")
GTHD.set(12, 3, "tree")
GTHD.set(13, 3, "tree")
GTHD.set(12, 2, "tree")
GTHD.set(13, 2, "tree")

GTHD.set(12, 8, "AD")
GTHD.set(12, 7, "AD")
GTHD.set(12, 6, "AD")
