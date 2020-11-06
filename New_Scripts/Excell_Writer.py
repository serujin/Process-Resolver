import xlsxwriter
import Constants

class Writer():
    def __init__(self, name, CPUS, debug = False):
        self.fill_data(CPUS)
        self.debug = debug
        self.worksheets = []
        self.name = name + ".xlsx"
        self.init_document()
        self.write_data()
        self.show_data()
    
    def show_data(self):
        for cpu in self.cpus:
            if self.debug:
                print("--------------------------------------")
                for i in cpu.history[0]:
                    print(i)
                print("--------------------------------------")
    
    def init_document(self):
        self.workbook = xlsxwriter.Workbook(self.name)
        self.init_worksheets()
        self.init_formats()

    def init_worksheets(self):
        self.write_historial()
        for algorithm in self.get_algorithms_name():
            self.worksheets.append(self.workbook.add_worksheet(algorithm))
            self.process_count = len(self.history[0])
        for worksheet in self.worksheets:
            worksheet.set_column('A:ZZ', 3)
            self.format_worksheet(worksheet)

    def init_formats(self):
        self.init_strikeout_format()
    
    def set_format_centered(self, data_format):
        data_format.set_center_across()

    def get_algorithms_name(self):
        names = []
        for algorithm in self.algs:
            if algorithm == Constants.FIFO:
                names.append("FIFO")
            if algorithm == Constants.SJF:
                names.append("SJF")
            if algorithm == Constants.SRTF:
                names.append("SRTF")
            if algorithm == Constants.RR:
                names.append("RR")
        return names

    def fill_data(self, CPU_data):
        self.cpus = []
        self.algs = []
        for i in CPU_data:
            self.cpus.append(i[0])
            self.algs.append(i[1])
        self.has_IO = False 
        for states in self.cpus[0].history:
            if Constants.ON_IO in states[0]:
                self.has_IO = True

    def write_data(self):
        for i in range(len(self.worksheets)):
            self.update_historial(i)
            self.worksheet = self.worksheets[i]
            self.width = len(self.double_dimension_historial)
            self.height = self.process_count
            self.current_column = 0
            self.current_cpu_row = 0
            self.current_io_row = 0
            for j in range(self.width):
                self.current_column += 1
                self.write_cpu(j)
                self.write_cpu_queue(j)
                if self.has_IO:
                    self.write_io(j)
                    self.write_io_queue(j)
        self.workbook.close()

    def write_historial(self):
        self.double_dimension_historial = self.cpus[0].history
        self.history = []
        self.durations = []
        for history in self.double_dimension_historial:
            self.history.append(history[0])
            self.durations.append(history[1])
    
    def update_historial(self, current_cpu):
        self.double_dimension_historial = self.cpus[current_cpu].history
        self.history = []
        self.durations = []
        for history in self.double_dimension_historial:
            self.history.append(history[0])
            self.durations.append(history[1])

    def write_cpu(self, current_time):
        index = self.get_cpu_from_current_time(current_time)
        if index > -1:
            self.write_character(index + 1, self.current_column, self.get_character_from_index(index))
        self.write_character(self.height + 1, self.current_column, self.current_column - 1)

    def write_cpu_queue(self, current_time):
        if self.current_column == self.width:
            self.write_character(self.height + self.current_cpu_row + 4, 2,                     "-", self.strikeout_format)
            self.write_character(self.height + self.current_cpu_row + 4, 1, self.current_column - 1                       )
            return
        last_indexes = []
        if current_time > 0:
            last_indexes = self.get_indexes_with_state(current_time - 1, Constants.ON_CPU_QUEUE)
        next_cpu_index = -1
        if self.current_column < self.width:
            next_cpu_index = self.get_cpu_from_current_time(current_time + 1) 
        current_cpu_queue_column = 0
        indexes = self.get_indexes_with_state(current_time, Constants.ON_CPU_QUEUE)
        if len(indexes) > 0:
            if not indexes == last_indexes:
                self.current_cpu_row += 1
            for index in indexes:
                if not indexes == last_indexes or next_cpu_index > -1:
                    current_cpu_queue_column += 1
                    character = str(self.get_character_from_index(index)) + str(self.durations[current_time][index])
                    if index == next_cpu_index:
                        self.write_character(self.height + self.current_cpu_row + 3, 1 + current_cpu_queue_column, character, self.strikeout_format)
                    else:
                        self.write_character(self.height + self.current_cpu_row + 3, 1 + current_cpu_queue_column, character)
                    self.write_character(self.height + self.current_cpu_row + 3,                                1,          self.current_column - 1)

    def write_io(self, current_time):
        index = self.get_io_from_current_time(current_time)
        if index > -1:
            self.write_character(index + 1, self.current_column + self.width + 1, self.get_character_from_index(index))
        self.write_character(self.height + 1, self.current_column + self.width + 1, self.current_column - 1)

    def write_io_queue(self, current_time):
        if self.current_column == self.width:
            self.write_character(self.height + self.current_io_row + 4, self.width + 3,                     "-", self.strikeout_format)
            self.write_character(self.height + self.current_io_row + 4, self.width + 2, self.current_column - 1                       )
            return
        last_indexes = []
        if current_time > 0:
            last_indexes = self.get_indexes_with_state(current_time - 1, Constants.ON_IO_QUEUE)
        next_io_index = -1
        if self.current_column < self.width:
            next_io_index = self.get_io_from_current_time(current_time + 1) 
        current_io_queue_column = 0
        indexes = self.get_indexes_with_state(current_time, Constants.ON_IO_QUEUE)
        if len(indexes) > 0:
            if not indexes == last_indexes:
                self.current_io_row += 1
            for index in indexes:
                if not indexes == last_indexes or next_io_index > -1:
                    current_io_queue_column += 1
                    character = str(self.get_character_from_index(index)) + str(self.durations[current_time][index])
                    if index == next_io_index:
                        self.write_character(self.height + self.current_io_row + 2, 1 + current_io_queue_column, character, self.strikeout_format)
                    else:
                        self.write_character(self.height + self.current_io_row + 2, self.current_column + self.width + 1 + current_io_queue_column, character)
                    self.write_character(self.height + self.current_io_row + 2, self.current_column + self.width + 2,          self.current_column - 1)

    def get_indexes_with_state(self, current_time, state):
        indexes = []
        states = self.history[current_time]
        for i in range(len(states)):
            if states[i] == state:
                indexes.append(i)
        return indexes

    def get_cpu_from_current_time(self, current_time):
        index = -1
        indexes = self.get_indexes_with_state(current_time, Constants.ON_CPU)
        if len(indexes) > 0:
            index = indexes[0]
        return index

    def get_io_from_current_time(self, current_time):
        index = -1
        indexes = self.get_indexes_with_state(current_time, Constants.ON_IO)
        if len(indexes) > 0:
            index = indexes[0]
        return index

    def format_worksheet(self, worksheet):
        self.center = self.workbook.add_format()
        self.center.set_center_across()
        for process in range(self.process_count):
            worksheet.conditional_format(Constants.RANGES[process][0], {"type":"no_blanks", "format" : self.workbook.add_format({"color" : "white", "bg_color": Constants.RANGES[process][1]})})

    def get_character_from_index(self, index):
        return chr(ord('@') + index + 1)

    def write_character(self, row, column, character, data_format = None):
        if not data_format == None:
            self.worksheet.write(row, column, character, data_format)
        else:
            self.worksheet.write(row, column, character, self.center)

    def init_strikeout_format(self):
        self.strikeout_format = self.workbook.add_format()
        self.strikeout_format.set_font_strikeout()
        self.set_format_centered(self.strikeout_format)