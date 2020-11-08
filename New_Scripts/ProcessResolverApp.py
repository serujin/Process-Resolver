from Process import Process
from CPU import CPU
from Excell_Writer import Writer
from FIFO import FIFO
import Constants

def get_exercise_one_processes(): #EJERCICIO 1 WORKS :)                                                    
    return [
        Process("A", 0, 3),
        Process("B", 2, 2),
        Process("C", 4, 4),
        Process("D", 1, 1),
        Process("E", 0, 2),
        Process("F", 2, 10),
        Process("G", 3, 3)
    ]
def get_exercise_two_processes(): #EJERCICIO 2                                                       
    return [
        Process("A", 0, 3, Constants.LOW_PRIORITY),
        Process("B", 2, 2, Constants.TOP_PRIORITY),
        Process("C", 4, 4, Constants.MID_PRIORITY),
        Process("D", 1, 1, Constants.TOP_PRIORITY),
        Process("E", 0, 2, Constants.MID_PRIORITY),
        Process("F", 2, 10, Constants.TOP_PRIORITY),
        Process("G", 3, 3, Constants.LOW_PRIORITY)
    ]
def get_exercise_three_processes(): #EJERCICIO 3                                                       
    return [
        Process("A", 0, 3, Constants.LOW_PRIORITY, [[1,5]]),
        Process("B", 2, 2, Constants.TOP_PRIORITY, [[1,1]]),
        Process("C", 4, 4, Constants.MID_PRIORITY, [[3,2]]),
        Process("D", 1, 1, Constants.TOP_PRIORITY),
        Process("E", 0, 2, Constants.MID_PRIORITY),
        Process("F", 2, 10, Constants.TOP_PRIORITY, [[2,1], [5,4]]),
        Process("G", 3, 3, Constants.LOW_PRIORITY, [[1,10]])
    ]
'''
def get_processes(): #TEST ALGORITMOS SIMPLES                                                      
    return [
        Process("A", 0, 3),
        Process("B", 2, 6),
        Process("C", 4, 4),
        Process("D", 6, 5),
        Process("E", 8, 2)  
    ] 
'''     
def get_exercise_one():
    return [
        [CPU(Constants.FIFO, get_exercise_one_processes()), Constants.FIFO],
        [CPU(Constants.SJF, get_exercise_one_processes()), Constants.SJF],
        [CPU(Constants.SRTF, get_exercise_one_processes()), Constants.SRTF],
        [CPU(Constants.RR, get_exercise_one_processes(), 3), Constants.RR]
    ]
def get_exercise_two():
    return [
        [CPU(Constants.FIFO, get_exercise_two_processes()), Constants.FIFO],
        [CPU(Constants.SJF, get_exercise_two_processes()), Constants.SJF],
        [CPU(Constants.SRTF, get_exercise_two_processes()), Constants.SRTF],
        [CPU(Constants.RR, get_exercise_two_processes(), 3), Constants.RR]
    ]
def get_exercise_three():
    return [
        [CPU(Constants.FIFO, get_exercise_three_processes()), Constants.FIFO],
        [CPU(Constants.SJF, get_exercise_three_processes()), Constants.SJF],
        [CPU(Constants.SRTF, get_exercise_three_processes()), Constants.SRTF],
        [CPU(Constants.RR, get_exercise_three_processes(), 4), Constants.RR]
    ]
    
Writer("Ejercicio_1", get_exercise_one())
Writer("Ejercicio_2", get_exercise_two())
Writer("Ejercicio_3", get_exercise_three())