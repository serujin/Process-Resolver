from Process import Process
from CPU import CPU
import Utils
import Constants

p1 = Process("A", 0, 3)
p2 = Process("B", 2, 6)
p3 = Process("C", 4, 4)
p4 = Process("D", 6, 5)
p5 = Process("E", 8, 2)

CPU(Constants.SRTF, [p1, p2, p3, p4, p5])