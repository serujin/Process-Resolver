import Constants
from FIFO import FIFO
from SJF import SJF
from SRTF import SRTF
from RR import RR

class CPU():
    def __init__(self, algorithm, processes, quantum = -1):
        self.__processes = processes
        self.__start(algorithm, quantum)

    def __start(self, algorithm, quantum):
        if algorithm == Constants.FIFO:
            self.__history = FIFO(self.__processes).history
        if algorithm == Constants.SJF:
            self.__history = SJF(self.__processes).history
        if algorithm == Constants.SRTF:
            self.__history = SRTF(self.__processes).history
        if algorithm == Constants.RR:
            self.__history = RR(self.__processes, quantum).history

    def get_history(self):
        return self.__history
