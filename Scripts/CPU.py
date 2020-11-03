from Process import Process

'''
Need to do:
FIFO
SJF
SRTF
RR
'''

class CPU():
    def __init__(self, algorithm, *processes, quantum = None):
        self.__init_all()
        self.__fill_processes(processes)
        self.__start(algorithm, quantum)

    def __init_all(self):
        self.__processes = []
        self.__history = [[]]

    def __fill_processes(self, *processes):
        for process in processes:
            self.__processes.append(process)

    def __start(self, algorithm, quantum):
        if algorithm == 0:
            self.__start_fifo()
        if algorithm == 1:
            self.__start_sjf()
        if algorithm == 2:
            self.__start_srtn()
        if algorithm == 3:
            self.__start_rr(quantum)

    def __start_fifo(self):
        pass

    def __start_sjf(self):
        pass
    
    def __start_srtn(self):
        pass
    
    def __start_rr(self, quantum):
        pass   
