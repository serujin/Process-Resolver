from Process import Process
from CPU import CPU
from Excell_Writer import Writer
import Utils
import Constants

def get_processes():
    return [
        Process("A", 0, 3, Constants.MID_PRIORITY),
        Process("B", 2, 6, Constants.MID_PRIORITY),
        Process("C", 2, 7, Constants.MID_PRIORITY),
        Process("D", 6, 5, Constants.MID_PRIORITY),
        Process("E", 8, 2, Constants.TOP_PRIORITY)
    ]

def get_exercises():
    return [
        CPU(Constants.FIFO, get_processes()),
        CPU(Constants.SJF, get_processes()),
        CPU(Constants.SRTF, get_processes()),
        CPU(Constants.RR, get_processes(), 2)
    ]

Writer("Ejercicio_1", get_exercises())