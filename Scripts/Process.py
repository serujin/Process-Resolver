import Constants

class Process():
    #io should be [[]] -> time to exit, time in io
    def __init__(self, id, arrival, duration, priority = None, io = None):
        self.__id = id
        self.__arrival = arrival
        self.__duration = duration
        self.__priority = priority
        self.__current_io = 0
        self.__max_duration = duration
        self.__io = io
        self.__state = Constants.NOT_ARRIVED

    def get_id(self):
        return self.__id

    def get_arrival(self):
        return self.__arrival

    def get_duration(self):
        return self.__duration

    def get_priority(self):
        return self.__priority

    def get_io(self):
        return self.__io

    def get_state(self):
        return self.__state

    def set_state(self, state):
        self.__state = state   

    def cpu_tick(self, time):
        self.__duration -= 1
        if self.__duration == 0:
            self.__state = Constants.ENDED
            return True
        if self.has_to_go_io(time):
            self.__state = Constants.ON_IO_QUEUE
            return True
        return False

    def io_tick(self):
        if self.__io[self.__current_io][1] == 0:
            self.__state = Constants.ON_CPU_QUEUE
            self.__current_io += 1
            return True
        self.__io[self.__current_io][1] -= 1
        return False

    def has_ended(self):
        return self.__duration < 1

    def has_to_go_io(self, time):
        if self.__io == None:
            return False
        if self.__current_io > (len(self.__io) - 1):
            return False
        return (self.__io[self.__current_io][0]) == (self.__max_duration - self.__duration)

    def has_io_ended(self):
        return self.__io[self.__current_io][1] < 1

    def has_priority(self):
        return self.__priority != None

    def has_IO(self):
        return self.__io != None

    def show(self):
        print("Process : " + self.__id + " || Arrival : "  + str(self.__arrival) + " || Duration : " +  str(self.__duration) + " || Prioridad : " +  str(self.__priority) + " || IO : " + str(self.__io) + " || State : " + str(self.__state))