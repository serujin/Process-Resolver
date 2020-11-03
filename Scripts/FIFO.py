import Utils
import Constants
from Process import Process

'''
1. Check for new Processes
2. Fill CPU
3. Fill CPU Queue
4. Fill IO
5. Fill IO Queue
6. Fill history
'''

class FIFO():
    def __init__(self, processes):
        self.__processes = processes
        self.__init_all()

    def __init_all(self):
        self.__time = 0
        self.__cpu_queue = []
        self.__io_queue = []
        self.__history = [[]]

    def __start(self):
        while not Utils.has_to_stop(self.__processes):
            pass

    def __check_for_new_arrivals(self):
        arrivals = Utils.get_new_arrivals(self.__processes, self.__time)
        if not len(arrivals) == 0:
            pass
    
