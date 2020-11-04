from Process import Process
from Non_Expulsive import Non_Expulsive
from Expulsive import Expulsive
import Constants

class CPU():
    def __init__(self, algorithm, processes, quantum = -1):
        self.__init_all()
        self.__processes = processes
        self.__start(algorithm, quantum)

    def __init_all(self):
        self.__processes = []

    def __start(self, algorithm, quantum):
        if algorithm == Constants.FIFO:
            self.__start_fifo()
        if algorithm == Constants.SJF:
            self.__start_sjf()
        if algorithm == Constants.SRTF:
            self.__start_srtf()
        if algorithm == Constants.RR:
            self.__start_rr(quantum)

    def __start_fifo(self):
        self.__history = Non_Expulsive(self.__processes, False).get_history()

    def __start_sjf(self):
        self.__history = Non_Expulsive(self.__processes, True).get_history()
    
    def __start_srtf(self):
        self.__history = Expulsive(self.__processes, True).get_history()
    
    def __start_rr(self, quantum):
        self.__history = Expulsive(self.__processes, False, quantum).get_history()

    def get_history(self):
        return self.__history
