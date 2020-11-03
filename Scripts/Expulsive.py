import Utils
import Constants
from Process import Process

class Expulsive():
    def __init__(self, processes, duration_matters, quantum = -1):
        self.__processes = processes
        self.__duration_matters = duration_matters
        self.__quantum = quantum
        self.__ids = Utils.get_processes_ids(self.__processes)
        self.__ids.sort()
        self.__init_all()
        self.__start()

    def __init_all(self):
        self.__time = 0
        self.__cpu = None
        self.__io = None
        self.__cpu_queue = []
        self.__io_queue = []
        self.__history = []

    def __start(self):
        while not Utils.has_to_stop(self.__processes):
            self.__check_if_cpu_should_change()
            self.__fill_cpu_queue()
            self.__fill_cpu()
            self.__fill_io_queue()
            self.__fill_io()
            self.__fill_history()
            self.__time += 1
        for i in range(len(self.__processes)):
            for j in self.__history:
                if j[i] == Constants.ENDED:
                    j[i] = Constants.ON_CPU
                    break
        end = []
        for i in range(len(self.__processes)):
            end.append(Constants.ENDED)
        self.__history.append(end)
        for i in self.__history:
            print(i)

    def __fill_cpu_queue(self):
        processes = Utils.get_new_arrivals(self.__processes, self.__time)
        self.__cpu_queue += processes
        for process in self.__cpu_queue:
            process.set_state(Constants.ON_CPU_QUEUE)
        self.__cpu_queue = Utils.order_by_priority(self.__cpu_queue, self.__duration_matters)

    def __check_if_cpu_should_change(self):
        if not self.__cpu == None:
            if len(self.__cpu_queue) > 0:
                print("Compared : " + str(self.__cpu_queue[0].get_duration()) + " < " + str(self.__cpu.get_duration()) + " = " + str(self.__cpu_queue[0].get_duration() < self.__cpu.get_duration()))
                if self.__cpu_queue[0].get_duration() < self.__cpu.get_duration():
                    self.__cpu_queue.append(self.__cpu)
                    self.__cpu = None 
                    print("changed")

    def __fill_cpu(self):
        if self.__cpu == None:
            if len(self.__cpu_queue) > 0:
                self.__cpu = self.__cpu_queue[0]
                self.__cpu_queue.remove(self.__cpu_queue[0])
                self.__cpu.set_state(Constants.ON_CPU)
                if not self.__cpu == None:
                    if self.__cpu.cpu_tick(self.__time, self.__quantum):
                        self.__cpu = None    
        elif self.__cpu.cpu_tick(self.__time, self.__quantum):
            self.__cpu = None

    def __fill_io_queue(self):
        for process in self.__processes:
            if process.get_state() == Constants.ON_IO_QUEUE and process not in self.__io_queue:
                self.__io_queue.append(process)
        self.__io_queue = Utils.order_by_priority(self.__io_queue, False) #Maybe have to delete this later to do 
                                                                            #full FIFO IO QUEUE
    def __fill_io(self):
        if self.__io == None:
            if len(self.__io_queue) > 0:
                self.__io = self.__io_queue[0]
                self.__io_queue.remove(self.__io_queue[0])
                self.__cpu.set_state(Constants.ON_IO)
                if not self.__io == None:
                   if self.__io.io_tick(self.__time):
                       self.__io = None 
        elif self.__io.io_tick(self.__time):
            self.__io = None 

    def __fill_history(self):
        temp = []
        print("iteration : " + str(self.__time))
        for _id in self.__ids:
            for process in self.__processes:
                if process.get_id() == _id:
                    print("added state : " + str(process.get_state()) + " to the id : " + str(_id) )
                    temp.append(process.get_state())
        self.__history.append(temp)