from Process import Process
from CPU import CPU
from Excell_Writer import Writer
import Utils
import Constants

def get_processes():
    return [
        Process("A", 0, 3),
        Process("B", 2, 6),
        Process("C", 4, 4),
        Process("D", 6, 5),
        Process("E", 8, 2)
    ]

def get_exercises():
    return [
        CPU(Constants.FIFO, get_processes()),
        CPU(Constants.SJF, get_processes()),
        CPU(Constants.SRTF, get_processes()),
        CPU(Constants.RR, get_processes(), 2)
    ]

Writer("Ejercicio_1", get_exercises())