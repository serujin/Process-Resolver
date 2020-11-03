import Constants

class Process():
    def __init__(self, id, arrival, duration, priority = None, io = None):
        self.__id = id
        self.__arrival = arrival
        self.__duration = duration
        self.__priority = priority
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

    def has_ended(self):
        return self.__duration < 1

    def has_priority(self):
        return self.__priority != None

    def has_IO(self):
        return self.__io != None

    def show(self):
        print(self.__id, self.__arrival, self.__duration, self.__priority, self.__io, self.__state)