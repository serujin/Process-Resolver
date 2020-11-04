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