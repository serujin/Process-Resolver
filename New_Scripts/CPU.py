import Constants
from FIFO import FIFO
from SJF import SJF
from SRTF import SRTF
from RR import RR

class CPU():
    def __init__(self, algorithm, processes, quantum = -1):
        self.processes = processes
        self.start(algorithm, quantum)

    def start(self, algorithm, quantum):
        if algorithm == Constants.FIFO:
            self.history = FIFO(self.processes).history
        if algorithm == Constants.SJF:
            self.history = SJF(self.processes).history
        if algorithm == Constants.SRTF:
            self.history = SRTF(self.processes).history
        if algorithm == Constants.RR:
            self.history = RR(self.processes, quantum).history
