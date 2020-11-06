from Process import Process
from CPU import CPU
from Excell_Writer import Writer
from FIFO import FIFO
import Constants
'''
def get_processes():                                                         
    return [
        Process("A", 0, 3, Constants.LOW_PRIORITY, [[1,5]]),
        Process("B", 2, 2, Constants.TOP_PRIORITY, [[1,1]]),
        Process("C", 4, 4, Constants.MID_PRIORITY, [[3,2]]),
        Process("D", 1, 1, Constants.TOP_PRIORITY),
        Process("E", 0, 2, Constants.MID_PRIORITY),
        Process("F", 2, 10, Constants.TOP_PRIORITY, [[2,1], [5,4]]),    
        Process("G", 3, 3, Constants.LOW_PRIORITY, [[1,10]])
    ]
''' 
def get_processes():
    return [
        Process("A", 0, 3, Constants.TOP_PRIORITY),
        Process("B", 3, 6),
        Process("C", 4, 4),
        Process("D", 6, 5),
        Process("E", 8, 2),
        Process("F", 2, 6),
        Process("G", 4, 4),
        Process("H", 6, 5),
        Process("I", 6, 5),
        Process("J", 6, 5)
    ]
def get_exercises():
    return [
        [CPU(Constants.FIFO, get_processes()), Constants.FIFO],
        [CPU(Constants.SJF, get_processes()), Constants.SJF],
        [CPU(Constants.SRTF, get_processes()), Constants.SRTF],
        [CPU(Constants.RR, get_processes(), 2), Constants.RR]
    ]

Writer("Ejercicio_1", get_exercises())