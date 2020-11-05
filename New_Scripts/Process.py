import Constants

class Process():
    def __init__(self, id, arrival, duration, priority = Constants.NAN_PRIORITY, io = None):
        self.id = id
        self.arrival = arrival
        self.duration = duration
        self.priority = priority
        self.io = io
        self.remaining_duration = duration
        self.current_io = 0
        self.state = Constants.NOT_ARRIVED

    def __str__(self):
        return "Process : " + self.id + " || Remaining Duration : " + str(self.remaining_duration) + " || IO : " + str(self.io) + " || State : " + str(self.state)

    def cpu_tick(self):
        self.remaining_duration -= 1
        return self.remaining_duration == 0
            
    def io_tick(self):
        self.io[self.current_io][1] -= 1
        return self.io[self.current_io][1] == 0

    def has_to_go_to_io(self):
        if not self.has_io():
            return False
        if self.current_io > len(self.io) - 1:
            return False
        return self.io[self.current_io][0] == self.duration - self.remaining_duration

    def current_io_ended(self):
        self.current_io += 1

    def has_ended(self):
        return self.remaining_duration == 0

    def has_priority(self):
        return not self.priority == None

    def has_io(self):
        return not self.io == None