#Processes states
NOT_ARRIVED = 0
ON_CPU = 1
ON_CPU_QUEUE = 2
ON_IO = 3
ON_IO_QUEUE = 4
ENDED = 5
#Processes priorities:
LOW_PRIORITY = 3
MID_PRIORITY = 2
TOP_PRIORITY = 1
NAN_PRIORITY = 0
#CPU algorithms
FIFO = 0
SJF = 1
SRTF = 2
RR = 3
#Letter colors
LETTER_COLORS = {
    0 : '#FF0000',
    1 : '#FF7B00',
    2 : '#FFCC00',
    3 : '#88FF00',
    4 : '#00FF44',
    5 : '#00FFD0',
    6 : '#00D9FF',
    7 : '#005EFF',
    8 : '#0D00FF',
    9 : '#7300FF',
    10 : '#CC00FF',
    11 : '#FF00EA',
    12 : '#FF007B'
}
RANGES = [
    [  "B2:ZZ2", '#B71C1C'],
    [  "B3:ZZ3", '#880E4F'],
    [  "B4:ZZ4", '#4A148C'],
    [  "B5:ZZ5", '#311B92'],
    [  "B6:ZZ6", '#1A237E'],
    [  "B7:ZZ7", '#0D47A1'],
    [  "B8:ZZ8", '#01579B'],
    [  "B9:ZZ9", '#01579B'],
    ["B10:ZZ10", '#006064'],
    ["B11:ZZ11", '#004D40'],
    ["B12:ZZ12", '#1B5E20'],
    ["B13:ZZ13", '#33691E'],
    ["B14:ZZ14", '#827717'],
    ["B15:ZZ15", '#F57F17'],
]