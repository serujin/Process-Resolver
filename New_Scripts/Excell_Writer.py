import xlsxwriter
import Constants

class Writer():
    def __init__(self, name, CPUS, debug = False):
        self.__CPUS = CPUS
        self.__debug = debug
        self.__worksheet_number = len(CPUS)
        self.__worksheets = []
        self.__name = name + ".xlsx"
        self.__show_data()
        self.__init_document()
        self.__write_data()
    
    def __show_data(self):
        for cpu in self.__CPUS:
            if self.__debug:
                print("--------------------------------------")
                for i in cpu.get_history():
                    print(i)
                print("--------------------------------------")
    
    def __init_document(self):
        self.__workbook = xlsxwriter.Workbook(self.__name)
        for i in range(self.__worksheet_number):
            self.__worksheets = self.__workbook.add_worksheet("Algoritmo_" + str(i + 1))
        for i in range(self.__worksheet_number):
            worksheet = self.__workbook.get_worksheet_by_name('Algoritmo_' + str(i + 1))
            worksheet.set_column('A:ZZ', 3)
        self.__init_formats()

    def __write_data(self):
        cpu = ["C", "P", "U"]
        #io = ["E", "/", "S"]
        queue = ["C", "O", "L", "A", "-"]
        cpu_queue = queue + cpu
        #io_queue = queue + io
        for i in range(self.__worksheet_number):
            worksheet = self.__workbook.get_worksheet_by_name('Algoritmo_' + str(i + 1))
            for j in range(len(cpu)):
                worksheet.write(1, j + 1, cpu[j], self.__number_guide_format) 
            for k in range(len(cpu_queue)):
                worksheet.write(9, k + 1, cpu_queue[k], self.__number_guide_format) 
            history = self.__CPUS[i].get_history()
            width = len(history)
            height = len(history[0])
            for column in range(width):
                self.__write_cpu_queue(worksheet, history, column, height)
                if Constants.ON_IO in history:
                    self.__write_io_queue(worksheet, history, column, height, width)
                for row in range(height):
                    state = history[column][row]
                    if state == Constants.ON_CPU:
                        self.__write_cpu(worksheet, row, column)
                    if state == Constants.ON_IO:
                        self.__write_io(worksheet, row, column, width)
        self.__workbook.close()
    
    def __write_cpu(self, worksheet, row, column):
        _format = self.__get_format(row)
        worksheet.write(row + 2, column + 1, chr(ord('@') + row + 1), _format)

    def __write_cpu_queue(self, worksheet, history, column, height):
        states = history[column]
        if not column == len(history) - 1:
            next_states = history[column + 1]
        else:
            next_states = [123] 
        worksheet.write(height + 2, column + 1, column, self.__number_guide_format)
        worksheet.write(len(states) + column + 5, 1, column,self.__number_guide_format) 
        number = -1
        for state in self.get_cpu_queue_row_formatted(states):
            number += 1
            _format = self.__number_guide_format
            #if next_states[number] == Constants.ON_CPU: #NEED TO FIX FORMAT
                #_format = self.__enter_to_cpu_format                
            worksheet.write(len(states) + column + 5, number + 2, state, _format)
        #worksheet.write(height + 1 + len(states), column + 1, column, self.__number_guide_format) #Writes CPU QUEUE NUMBERS
        #for i in range(len(states)):
            #if states[i] == Constants.ON_CPU_QUEUE:
                #queue.append(chr(ord('@') + i + 1))
        #for j in range(len(queue)):
            #_format = self.__get_format(ord(queue[j]) - 65)
            #worksheet.write(len(states) + j + 3, column + 1, queue[j], _format)

    def __write_io(self, worksheet, row, column, width):
        _format = self.__get_format(row)
        worksheet.write(row + 1, width + column + 2, chr(ord('@') + row + 1), _format)

    def __write_io_queue(self, worksheet, history, column, height, width):
        states = history[column]
        queue = []
        worksheet.write(height + 1, width + column + 2, column, self.__number_guide_format) 
        worksheet.write(height + 1 + len(states), width + column + 2, column, self.__number_guide_format) 
        for i in range(len(states)):
            if states[i] == Constants.ON_IO_QUEUE:
                queue.append(chr(ord('@') + i + 1))
        for j in range(len(queue)):
            _format = self.__get_format(ord(queue[j]) - 65)
            worksheet.write(len(states) + j + 3, width + column + 2, queue[j], _format)

    def __init_formats(self):
        self.__formats = []
        self.__number_guide_format = self.__workbook.add_format()
        self.__enter_to_cpu_format = self.__workbook.add_format()
        self.__number_guide_format.set_center_across()
        self.__enter_to_cpu_format.set_center_across()
        self.__enter_to_cpu_format.set_font_strikeout()
        for color in Constants.LETTER_COLORS.values():
            _format = self.__workbook.add_format()
            _format.set_center_across()
            _format.set_font_color('white')
            _format.set_bg_color(color)
            self.__formats.append(_format)

    def __get_format(self, row):
        return self.__formats[row]

    def get_cpu_queue_row_formatted(self, states):
        formatted_row = []
        for i in range(len(states)):
            if states[i] == Constants.ON_CPU_QUEUE:
                formatted_row.append(chr(ord('@') + i + 1))
        return formatted_row
