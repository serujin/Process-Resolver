from Process import Process
from abc import ABC, abstractmethod
import Constants

class Algorithm(ABC):
    def __init__(self, processes, quantum = -1):
        super().__init__()
        self.processes = processes
        self.cpu = None
        self.io = None
        self.cpu_queue = []
        self.io_queue = []
        self.history = []
        self.current_time = 0
        self.quantum = quantum
        self.current_quantum = -1

    def start(self):
        while not self.has_to_stop():
            self.main_loop()
            self.current_time += 1
        self.fill_history()

    def main_loop(self):
        self.update_logic()
        self.update_all_states()
        self.fill_history()
        self.cpu_tick()
        self.io_tick()
            
    @abstractmethod
    def update_logic(self):
        pass
    
    def fill_history(self):
        current_time_history = []
        current_durations_history = []
        for process in self.processes:
            current_time_history.append(process.state)
            current_durations_history.append(process.remaining_duration)
        history_time = [current_time_history, current_durations_history]
        self.history.append(history_time)

    def update_all_states(self):
        self.__update_cpu()
        self.__update_io()
        self.__update_cpu_queue()
        self.__update_io_queue()

    def __update_cpu(self):
        if not self.cpu_is_empty():
            self.cpu.state = Constants.ON_CPU    
    
    def __update_cpu_queue(self):
        if not self.cpu_queue_is_empty():
            for process in self.cpu_queue:
                process.state = Constants.ON_CPU_QUEUE   

    def update_io_logic(self):
        if self.io_is_empty() and not self.io_queue_is_empty():
            self.fill_io()

    def __update_io(self):
        if not self.io_is_empty():
            self.io.state = Constants.ON_IO    
    
    def __update_io_queue(self):
        if not self.io_queue_is_empty():
            for process in self.io_queue:
                process.state = Constants.ON_IO_QUEUE

    def cpu_tick(self):
        if self.cpu_is_empty():
            return
        if self.cpu.cpu_tick():
            self.cpu.state = Constants.ENDED
            self.empty_cpu()

    def io_tick(self):
        if self.io_is_empty():
            return
        if self.io.io_tick():
            self.io.state = Constants.ON_CPU_QUEUE
            self.empty_io()

    def has_to_stop(self):
        ended = True
        for process in self.processes:
            if not process.has_ended():
                ended = False
        return ended
    
    def get_new_arrivals(self):
        arrivals = []
        for process in self.processes:
            if process.arrival == self.current_time:
                arrivals.append(process)
        return arrivals

    def get_processes_by_priority(self, processes, priority):
        processes_to_return = []
        for process in processes:
            if process.has_priority() and process.priority == priority:
                processes_to_return.append(process)
        return processes_to_return

    def get_processes_ordered_alphabetically(self, processes):
        ordered_processes_to_return = []
        ids = []
        for process in processes:
            ids.append(process.id)
        ids.sort()
        for id in ids:
            for process in processes:
                if id == process.id and process not in ordered_processes_to_return:
                    ordered_processes_to_return.append(process)
        return ordered_processes_to_return

    def get_processes_ordered_from_lowest_to_highest_duration(self, processes):
        ordered_processes_to_return = []
        duration = []
        for process in processes:
            duration.append(process.duration)
        duration.sort()
        for duration in duration:
            for process in processes:
                if duration == process.duration and process not in ordered_processes_to_return:
                    ordered_processes_to_return.append(process)
        return ordered_processes_to_return

    def cpu_is_empty(self):
        return self.cpu == None
    
    def io_is_empty(self):
        return self.io == None

    def cpu_queue_is_empty(self):
        return len(self.cpu_queue) == 0
        
    def io_queue_is_empty(self):
        return len(self.io_queue) == 0

    def fill_cpu_queue(self, processes):
        for process in processes:
            process.state = Constants.ON_CPU_QUEUE
        for process in self.processes:
            if process.state == Constants.ON_CPU_QUEUE and process not in self.cpu_queue:
                self.cpu_queue.append(process)

    def fill_cpu(self):
        self.current_quantum = -1
        self.cpu = self.cpu_queue[0]
        self.cpu_queue.remove(self.cpu)
    
    def fill_io(self):
        self.io = self.io_queue[0]
        self.io_queue.remove(self.io)

    def send_cpu_to_cpu_queue(self):
        self.cpu_queue.append(self.cpu)
        self.empty_cpu()

    def send_cpu_to_io_queue(self):
        self.io_queue.append(self.cpu)
        self.empty_cpu()

    def send_io_to_cpu_queue(self):
        self.cpu_queue.append(self.io)
        self.empty_io()

    def cpu_has_to_go_to_io(self):
        return self.cpu.has_to_go_to_io()

    def empty_cpu(self):
        self.cpu = None

    def empty_io(self):
        self.io.current_io_ended()
        self.io = None

    def queue_processes_are_identical(self, queue):
        if len(queue) == 0:
            return False
        durations = []
        priorities = []
        for process in queue:
            durations.append(process.remaining_duration)
            priorities.append(process.priority)
        duration_checker = durations[0]
        priorities_checker = priorities[0]
        for duration in durations:
            if not duration == duration_checker:
                return False 
        for priority in priorities:
            if not priority == priorities_checker:
                return False
        return True

    def get_ordered_queue(self, queue, duration, alphabetically):
        top_priority_queue = self.get_processes_by_priority(queue, Constants.TOP_PRIORITY)
        mid_priority_queue = self.get_processes_by_priority(queue, Constants.MID_PRIORITY)
        low_priority_queue = self.get_processes_by_priority(queue, Constants.LOW_PRIORITY)
        nan_priority_queue = self.get_processes_by_priority(queue, Constants.NAN_PRIORITY)
        if duration:
            top_priority_queue = self.get_processes_ordered_from_lowest_to_highest_duration(top_priority_queue)
            mid_priority_queue = self.get_processes_ordered_from_lowest_to_highest_duration(mid_priority_queue)
            low_priority_queue = self.get_processes_ordered_from_lowest_to_highest_duration(low_priority_queue)
            nan_priority_queue = self.get_processes_ordered_from_lowest_to_highest_duration(nan_priority_queue)
        if alphabetically or self.queue_processes_are_identical(queue) and self.quantum > 0: #If alphabetically cares delete this for RR
            top_priority_queue = self.get_processes_ordered_alphabetically(top_priority_queue)
            mid_priority_queue = self.get_processes_ordered_alphabetically(mid_priority_queue)
            low_priority_queue = self.get_processes_ordered_alphabetically(low_priority_queue)
            nan_priority_queue = self.get_processes_ordered_alphabetically(nan_priority_queue)
        return top_priority_queue + mid_priority_queue + low_priority_queue + nan_priority_queue