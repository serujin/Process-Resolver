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

    def init_formats(self):
        self.center = self.workbook.add_format()
        self.center.set_center_across()
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
            self.current_time = 0
            for j in range(self.width):
                self.current_column += 1
                self.write_cpu()
                self.write_queue(False)
                if self.has_IO:
                    self.write_io()
                    self.write_queue(True)
                self.current_time += 1
            self.format_worksheet(self.worksheets[i])
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

    def write_cpu(self):
        index = self.get_cpu_from_current_time(self.current_time)
        if index > -1:
            self.write_character(index + 2, self.current_column, self.get_character_from_index(index))
        
    def write_io(self):
        index = self.get_io_from_current_time(self.current_time)
        if index > -1:
            self.write_character(index + 2, self.current_column + self.width + 1, self.get_character_from_index(index))

    def write_queue(self, io):
        if io:
            self.write_io_queue()
        else:
            self.write_cpu_queue()
        
    def write_io_queue(self):
        io_number_column = self.width + 2
        io__queue_column = self.width + 3
        io_row = self.height + self.current_io_row + 5
        printed_queue = False
        if self.current_column == self.width:
            self.write_character(io_row, io__queue_column, "-", self.strikeout_format)
            self.write_character(io_row, io_number_column, self.current_time)
        else:
            current_column_io_queue = 0
            self.write_character(io_row, io_number_column, self.current_time)
            if self.current_time == 0:
                time_zero_io_index = self.get_io_from_current_time(self.current_time)
                if time_zero_io_index > -1:
                    current_column_io_queue += 1
                    character = str(self.get_character_from_index(time_zero_io_index)) + str(self.durations[self.current_time][time_zero_io_index])
                    self.write_character(io_row, io_number_column + current_column_io_queue, character, self.strikeout_format)
                for index in self.get_indexes_with_state(self.current_time, Constants.ON_IO_QUEUE):
                    printed_queue = True
                    current_column_io_queue += 1
                    character = str(self.get_character_from_index(index)) + str(self.durations[self.current_time][index])
                    self.write_character(io_row, io_number_column + current_column_io_queue, character)
            else:
                differences = self.get_differences_from_last_time(self.current_time)
                for index in range(len(differences)):
                    if differences[index] in [Constants.FROM_CPU_TO_IO, Constants.FROM_IO_QUEUE_TO_IO]:
                        current_column_io_queue += 1
                        character = str(self.get_character_from_index(index)) + str(self.durations[self.current_time][index])
                        self.write_character(io_row, io_number_column + current_column_io_queue, character, self.strikeout_format)
                        printed_queue = True
                        for index in self.get_indexes_with_state(self.current_time, Constants.ON_IO_QUEUE):
                            current_column_io_queue += 1
                            character = str(self.get_character_from_index(index)) + str(self.durations[self.current_time][index])
                            self.write_character(io_row, io_number_column + current_column_io_queue, character)
            last_time_queue = self.get_indexes_with_state(self.current_time - 1, Constants.ON_IO_QUEUE)
            curr_time_queue = self.get_indexes_with_state(self.current_time, Constants.ON_IO_QUEUE)
            if not last_time_queue == curr_time_queue and not printed_queue:
                for index in curr_time_queue:
                    current_column_io_queue += 1
                    character = str(self.get_character_from_index(index)) + str(self.durations[self.current_time][index])
                    self.write_character(io_row, io_number_column + current_column_io_queue, character)
            if current_column_io_queue > 0:
                self.write_character(io_row, io_number_column, self.current_time)
                self.current_io_row += 1

    def write_cpu_queue(self):
        cpu_number_column = 1
        cpu__queue_column = 2
        cpu_row = self.height + self.current_cpu_row + 5
        printed_queue = False
        if self.current_column == self.width:
            self.write_character(cpu_row, cpu__queue_column, "-", self.strikeout_format)
            self.write_character(cpu_row, cpu_number_column, self.current_time)
            self.last_row_after_cpu_queue = cpu_row + 1
        else:
            current_column_cpu_queue = 0
            self.write_character(cpu_row, cpu_number_column, self.current_time)
            if self.current_time == 0:
                time_zero_cpu_index = self.get_cpu_from_current_time(self.current_time)
                if time_zero_cpu_index > -1:
                    current_column_cpu_queue += 1
                    character = str(self.get_character_from_index(time_zero_cpu_index)) + str(self.durations[self.current_time][time_zero_cpu_index])
                    self.write_character(cpu_row, cpu_number_column + current_column_cpu_queue, character, self.strikeout_format)
                for index in self.get_indexes_with_state(self.current_time, Constants.ON_CPU_QUEUE):
                    printed_queue = True
                    current_column_cpu_queue += 1
                    character = str(self.get_character_from_index(index)) + str(self.durations[self.current_time][index])
                    self.write_character(cpu_row, cpu_number_column + current_column_cpu_queue, character)
            else:
                differences = self.get_differences_from_last_time(self.current_time)
                for index in range(len(differences)):
                    if differences[index] in [Constants.FROM_CPU_QUEUE_TO_CPU, Constants.FROM_ARRIVED_TO_CPU, Constants.FROM_IO_TO_CPU]:
                        current_column_cpu_queue += 1
                        character = str(self.get_character_from_index(index)) + str(self.durations[self.current_time][index])
                        self.write_character(cpu_row, cpu_number_column + current_column_cpu_queue, character, self.strikeout_format)
                        printed_queue = True
                        for index in self.get_indexes_with_state(self.current_time, Constants.ON_CPU_QUEUE):
                            current_column_cpu_queue += 1
                            character = str(self.get_character_from_index(index)) + str(self.durations[self.current_time][index])
                            self.write_character(cpu_row, cpu_number_column + current_column_cpu_queue, character)
            last_time_queue = self.get_indexes_with_state(self.current_time - 1, Constants.ON_CPU_QUEUE)
            curr_time_queue = self.get_indexes_with_state(self.current_time, Constants.ON_CPU_QUEUE)
            if not last_time_queue == curr_time_queue and not printed_queue:
                for index in curr_time_queue:
                    current_column_cpu_queue += 1
                    character = str(self.get_character_from_index(index)) + str(self.durations[self.current_time][index])
                    self.write_character(cpu_row, cpu_number_column + current_column_cpu_queue, character)
            if current_column_cpu_queue > 0:
                self.write_character(cpu_row, cpu_number_column, self.current_time)
                self.current_cpu_row += 1

    def get_differences_from_last_time(self, current_time):
        curr_states = self.history[current_time]
        last_states = self.history[current_time - 1]
        differences = []
        for i in range(len(curr_states)):
            differences.append(self.get_difference_between_states(last_states[i], curr_states[i]))
        return differences

    def get_difference_between_states(self, current_state, next_state):
        if self.current_time == 0 and current_state == Constants.ON_CPU:
            return Constants.FROM_ARRIVED_TO_CPU
        if current_state == Constants.NOT_ARRIVED:
            if next_state == Constants.ON_CPU:
                return Constants.FROM_ARRIVED_TO_CPU
            if next_state == Constants.ON_CPU_QUEUE:
                return Constants.FROM_ARRIVED_TO_CPU_QUEUE
        if current_state == Constants.ON_CPU_QUEUE:
            if next_state == Constants.ON_CPU:
                return Constants.FROM_CPU_QUEUE_TO_CPU
        if current_state == Constants.ON_CPU:
            if next_state == Constants.ON_CPU_QUEUE:
                return Constants.FROM_CPU_TO_CPU_QUEUE
            if next_state == Constants.ON_IO_QUEUE:
                return Constants.FROM_CPU_TO_IO_QUEUE
            if next_state == Constants.ON_IO:
                return Constants.FROM_CPU_TO_IO
            if next_state == Constants.ENDED:
                return Constants.FROM_CPU_TO_ENDED
        if current_state == Constants.ON_IO_QUEUE:
            if next_state == Constants.ON_IO:
                return Constants.FROM_IO_QUEUE_TO_IO
        if current_state == Constants.ON_IO:
            if next_state == Constants.ON_CPU:
                return Constants.FROM_IO_TO_CPU
            if next_state == Constants.ON_CPU_QUEUE:
                return Constants.FROM_IO_TO_CPU_QUEUE
        return Constants.NO_CHANGE

    def is_not_the_last_time(self):
        return not self.current_column == self.width
        
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
        for process in range(self.process_count):
            worksheet.conditional_format(Constants.RANGES[process][0], {"type":"no_blanks", "format":self.workbook.add_format({"color" : "white", "bg_color": Constants.RANGES[process][1]})})     
        black_bg_format = self.workbook.add_format({"bg_color":"#C0C0C0"})
        black_bg_format.set_center_across()
        red_bg_format = self.workbook.add_format({"bg_color":"#808080"})
        cyan_bg_format = self.workbook.add_format({"bg_color":"#E5E5E5"})
        red_bg_format.set_center_across()
        cyan_bg_format.set_center_across()
        if self.has_IO:
            final_length = (self.width * 2) + 3
        else:
            final_length = self.width + 2
        for i in range(final_length):
            self.write_character(0, i, " ", black_bg_format)
            self.write_character(self.height + 3, i, " ", black_bg_format)
            self.write_character(self.last_row_after_cpu_queue, i, " ", black_bg_format)
        for i in range(self.last_row_after_cpu_queue + 1):
            self.write_character(i, 0, " ", black_bg_format)
            if self.has_IO:
                self.write_character(i, (self.width * 2) + 2, " ", black_bg_format)
            self.write_character(i, self.width + 1, " ", black_bg_format)
        for i in range(self.width):
            self.write_character(1, i + 1, " ", red_bg_format)
            self.write_character(self.height + 4, i + 1, " ", red_bg_format)
            if self.has_IO:
                self.write_character(1, self.width + i + 2, " ", red_bg_format)
                self.write_character(self.height + 4, self.width + i + 2, " ", red_bg_format)
            
        cpu = ["C","P","U"]
        io = ["E","/","S"]
        queue = ["C","O","L","A","-"]
        repo = "GIT>>>"
        program = "PROCESS RESOLVER"
        for letter in range(len(program)):
            self.write_character(0, letter + 1, program[letter], black_bg_format)
        for letter in range(len(repo)):
            self.write_character(self.last_row_after_cpu_queue, letter + 1, repo[letter], black_bg_format)
        worksheet.write_url(self.last_row_after_cpu_queue, len(repo) + 1, 'https://github.com/selcox/Process-Resolver', black_bg_format, string='@')
        cpu_queue = queue + cpu
        io_queue = queue + io
        for i in range(len(cpu)):
            self.write_character(1, i + 1, cpu[i], red_bg_format)
            if self.has_IO:
                self.write_character(1, self.width + i + 2, io[i], red_bg_format)
        for i in range(len(cpu_queue)):
            self.write_character(self.height + 4, i + 1, cpu_queue[i], red_bg_format)
            if self.has_IO:
                self.write_character(self.height + 4, self.width + i + 2, io_queue[i], red_bg_format)
        for i in range(self.width):
            self.write_character(self.height + 2, i + 1, i, cyan_bg_format)
            if self.has_IO:
                self.write_character(self.height + 2, self.width + i + 2, i, cyan_bg_format)

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