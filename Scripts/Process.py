import Constants

class Process():
    #io should be [[]] -> time to exit, time in io
    def __init__(self, id, arrival, duration, priority = None, io = None):
        self.__id = id
        self.__arrival = arrival
        self.__duration = duration
        self.__priority = priority
        self.__current_io = 0
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

    def cpu_tick(self, time, quantum = -1):
        self.__duration -= 1
        if self.__duration == 0:
            self.__state = Constants.ENDED
            return True
        if self.has_to_go_io(time):
            print("Sended to IO " + str(self.__id))
            self.__state = Constants.ON_IO_QUEUE
            return True
        return False

    def io_tick(self):
        self.__io[self.__current_io][1] -= 1
        if self.__io[self.__current_io][1] == 0:
            self.__state = Constants.ON_CPU_QUEUE
            self.__current_io += 1
            return True
        return False

    def has_ended(self):
        return self.__duration < 1

    def has_to_go_io(self, time):
        if self.__io == None:
            return False
        return self.__io[self.__current_io][0] == time

    def has_io_ended(self):
        return self.__io[self.__current_io][1] < 1

    def has_priority(self):
        return self.__priority != None

    def has_IO(self):
        return self.__io != None

    def show(self):
        print(self.__id, self.__arrival, self.__duration, self.__priority, self.__io, self.__state)