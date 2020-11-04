from Process import Process
from CPU import CPU
from Excell_Writer import Writer
import Utils
import Constants

p1 = Process("A", 0, 3, Constants.LOW_PRIORITY)
p2 = Process("B", 2, 2, Constants.TOP_PRIORITY)
p3 = Process("C", 4, 4, Constants.MID_PRIORITY)
p4 = Process("D", 1, 1, Constants.TOP_PRIORITY)
p5 = Process("E", 0, 2, Constants.MID_PRIORITY)
p6 = Process("F", 2, 10, Constants.TOP_PRIORITY)
p7 = Process("G", 3, 3, Constants.LOW_PRIORITY)

writer1 = []
"--- FIFO ---"
writer1.append(CPU(Constants.FIFO, [p1, p2, p3, p4, p5, p6, p7]))
p1 = Process("A", 0, 3, Constants.LOW_PRIORITY)
p2 = Process("B", 2, 2, Constants.TOP_PRIORITY)
p3 = Process("C", 4, 4, Constants.MID_PRIORITY)
p4 = Process("D", 1, 1, Constants.TOP_PRIORITY)
p5 = Process("E", 0, 2, Constants.MID_PRIORITY)
p6 = Process("F", 2, 10, Constants.TOP_PRIORITY)
p7 = Process("G", 3, 3, Constants.LOW_PRIORITY)
"--- SJF ---"
writer1.append(CPU(Constants.SJF, [p1, p2, p3, p4, p5, p6, p7]))
p1 = Process("A", 0, 3, Constants.LOW_PRIORITY)
p2 = Process("B", 2, 2, Constants.TOP_PRIORITY)
p3 = Process("C", 4, 4, Constants.MID_PRIORITY)
p4 = Process("D", 1, 1, Constants.TOP_PRIORITY)
p5 = Process("E", 0, 2, Constants.MID_PRIORITY)
p6 = Process("F", 2, 10, Constants.TOP_PRIORITY)
p7 = Process("G", 3, 3, Constants.LOW_PRIORITY)
"--- SRTF ---"
writer1.append(CPU(Constants.SRTF, [p1, p2, p3, p4, p5, p6, p7]))
p1 = Process("A", 0, 3, Constants.LOW_PRIORITY)
p2 = Process("B", 2, 2, Constants.TOP_PRIORITY)
p3 = Process("C", 4, 4, Constants.MID_PRIORITY)
p4 = Process("D", 1, 1, Constants.TOP_PRIORITY)
p5 = Process("E", 0, 2, Constants.MID_PRIORITY)
p6 = Process("F", 2, 10, Constants.TOP_PRIORITY)
p7 = Process("G", 3, 3, Constants.LOW_PRIORITY)
"--- RR Q=3 ---"
writer1.append(CPU(Constants.RR, [p1, p2, p3, p4, p5, p6, p7], 3))

"NOW WITH IO" #DOESN'T SEEM TO BE WORKING
writer2 = []
p1 = Process("A", 0, 3, Constants.LOW_PRIORITY, [[1, 5]])
p2 = Process("B", 2, 2, Constants.TOP_PRIORITY, [[1, 1]])
p3 = Process("C", 4, 4, Constants.MID_PRIORITY, [[3, 2]])
p4 = Process("D", 1, 1, Constants.TOP_PRIORITY)
p5 = Process("E", 0, 2, Constants.MID_PRIORITY)
p6 = Process("F", 2, 10, Constants.TOP_PRIORITY, [[2, 1], [5, 4]])
p7 = Process("G", 3, 3, Constants.LOW_PRIORITY, [[1, 10]])

"--- FIFO ---"
writer2.append(CPU(Constants.FIFO, [p1, p2, p3, p4, p5, p6, p7]))
p1 = Process("A", 0, 3, Constants.LOW_PRIORITY, [[1, 5]])
p2 = Process("B", 2, 2, Constants.TOP_PRIORITY, [[1, 1]])
p3 = Process("C", 4, 4, Constants.MID_PRIORITY, [[3, 2]])
p4 = Process("D", 1, 1, Constants.TOP_PRIORITY)
p5 = Process("E", 0, 2, Constants.MID_PRIORITY)
p6 = Process("F", 2, 10, Constants.TOP_PRIORITY, [[2, 1], [5, 4]])
p7 = Process("G", 3, 3, Constants.LOW_PRIORITY, [[1, 10]])
"--- SJF ---"
writer2.append(CPU(Constants.SJF, [p1, p2, p3, p4, p5, p6, p7]))
p1 = Process("A", 0, 3, Constants.LOW_PRIORITY, [[1, 5]])
p2 = Process("B", 2, 2, Constants.TOP_PRIORITY, [[1, 1]])
p3 = Process("C", 4, 4, Constants.MID_PRIORITY, [[3, 2]])
p4 = Process("D", 1, 1, Constants.TOP_PRIORITY)
p5 = Process("E", 0, 2, Constants.MID_PRIORITY)
p6 = Process("F", 2, 10, Constants.TOP_PRIORITY, [[2, 1], [5, 4]])
p7 = Process("G", 3, 3, Constants.LOW_PRIORITY, [[1, 10]])
"--- SRTF ---"
writer2.append(CPU(Constants.SRTF, [p1, p2, p3, p4, p5, p6, p7]))
p1 = Process("A", 0, 3, Constants.LOW_PRIORITY, [[1, 5]])
p2 = Process("B", 2, 2, Constants.TOP_PRIORITY, [[1, 1]])
p3 = Process("C", 4, 4, Constants.MID_PRIORITY, [[3, 2]])
p4 = Process("D", 1, 1, Constants.TOP_PRIORITY)
p5 = Process("E", 0, 2, Constants.MID_PRIORITY)
p6 = Process("F", 2, 10, Constants.TOP_PRIORITY, [[2, 1], [5, 4]])
p7 = Process("G", 3, 3, Constants.LOW_PRIORITY, [[1, 10]])
"--- RR Q=4 ---"
writer2.append(CPU(Constants.RR, [p1, p2, p3, p4, p5, p6, p7], 4))

Writer("Ejercicio 1", writer1, True)
Writer("Ejercicio 1", writer2, True)