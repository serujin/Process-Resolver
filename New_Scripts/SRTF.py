from Algorithm import Algorithm
import Constants

class SRTF(Algorithm):
    def __init__(self, processes):
        super().__init__(processes)
        self.start()

    def update_logic(self):    
        self.update_all()

    def update_all(self):
        self.update_cpu_queue_logic()
        self.update_cpu_logic()
        self.update_io_queue_logic()
        self.update_io_logic()

    def update_cpu_queue_logic(self):
        new_processes = self.get_new_arrivals()
        self.fill_cpu_queue(new_processes)
        if self.queue_processes_are_identical(self.cpu_queue):
                self.cpu_queue = self.get_ordered_queue(self.cpu_queue, True)
        else:
            self.cpu_queue = self.get_ordered_queue(self.cpu_queue, True)

    def update_cpu_logic(self):
        if self.cpu_has_to_exit():
            self.send_cpu_to_cpu_queue()
            self.cpu_queue = self.get_ordered_queue(self.cpu_queue, True)
        if self.cpu_is_empty() and not self.cpu_queue_is_empty():
            self.fill_cpu()
        
    def update_io_queue_logic(self):
        if not self.cpu_is_empty() and self.cpu_has_to_go_to_io():
            self.send_cpu_to_io_queue()
            self.cpu_queue = self.get_ordered_queue(self.cpu_queue, False) #Maybe delete this and transfer to parent
            if not self.cpu_queue_is_empty():
                self.fill_cpu()

    def cpu_has_to_exit(self):
        if not self.cpu_is_empty() and not self.cpu_queue_is_empty():
            return self.cpu.remaining_duration > self.cpu_queue[0].remaining_duration or (self.cpu.priority > self.cpu_queue[0].priority and self.cpu.remaining_duration == self.cpu_queue[0].remaining_duration)
