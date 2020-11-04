import xlsxwriter

class Writer():
    def __init__(self, name, CPUS, debug = False):
        self.__CPUS = CPUS
        self.__debug = debug
        self.__worksheet_number = len(CPUS)
        self.__worksheets = []
        self.__name = name + ".xlsx"
        self.__show_data()
    
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
            self.__worksheets = self.__workbook.add_worksheet("Ejercicio " + str(i + 1))

    def __write_data(self):
        pass
        