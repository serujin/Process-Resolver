from Algorithm import Algorithm

class RR(Algorithm):
    def __init__(self, processes, quantum):
        super().__init__(processes, quantum - 1)
        self.start()

    def update_logic(self):    
        self.update_all()

    def update_all(self):
        if not self.cpu_is_empty():
            self.current_quantum += 1
        self.update_cpu_queue_logic()
        self.update_cpu_logic()
        self.update_io_queue_logic()
        self.update_io_logic()

    def update_cpu_queue_logic(self):
        new_processes = self.get_new_arrivals()
        self.fill_cpu_queue(new_processes)
        self.cpu_queue = self.get_ordered_queue(self.cpu_queue, False)

    def update_cpu_logic(self):
        if self.cpu_has_to_exit():
            self.send_cpu_to_cpu_queue()
            self.cpu_queue = self.get_ordered_queue(self.cpu_queue, False)
        if self.cpu_is_empty() and not self.cpu_queue_is_empty():
            self.fill_cpu()
        
    def update_io_queue_logic(self):
        if not self.cpu_is_empty() and self.cpu_has_to_go_to_io():
            self.send_cpu_to_io_queue()
            if not self.cpu_queue_is_empty():
                self.fill_cpu()

    def cpu_has_to_exit(self): 
        if not self.cpu_is_empty():
            return self.current_quantum == self.quantum 

    