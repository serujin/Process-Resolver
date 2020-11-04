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
        for i in range(self.__worksheet_number):
            worksheet = self.__workbook.get_worksheet_by_name('Algoritmo_' + str(i + 1))
            history = self.__CPUS[i].get_history()
            width = len(history)
            height = len(history[0])
            for column in range(width):
                self.__write_cpu_queue(worksheet, history, column, height)
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
        worksheet.write(row + 1, column + 1, chr(ord('@') + row + 1), _format)

    def __write_cpu_queue(self, worksheet, history, column, height):
        states = history[column]
        queue = []
        worksheet.write(height + 1, column + 1, column, self.__number_guide_format) 
        worksheet.write(height + 1 + len(states), column + 1, column, self.__number_guide_format) 
        for i in range(len(states)):
            if states[i] == Constants.ON_CPU_QUEUE:
                queue.append(chr(ord('@') + i + 1))
        for j in range(len(queue)):
            _format = self.__get_format(ord(queue[j]) - 65)
            worksheet.write(len(states) + j + 3, column + 1, queue[j], _format)

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
        self.__number_guide_format.set_center_across()
        for color in Constants.LETTER_COLORS.values():
            _format = self.__workbook.add_format()
            _format.set_center_across()
            _format.set_font_color('white')
            _format.set_bg_color(color)
            self.__formats.append(_format)

    def __get_format(self, row):
        return self.__formats[row]