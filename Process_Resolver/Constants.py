#Processes states
NOT_ARRIVED = 0
ON_CPU = 1
ON_CPU_QUEUE = 2
ON_IO = 3
ON_IO_QUEUE = 4
ENDED = 5
#Possible state changes
NO_CHANGE = -1
FROM_ARRIVED_TO_CPU = 0
FROM_ARRIVED_TO_CPU_QUEUE = 1
FROM_CPU_QUEUE_TO_CPU = 2
FROM_CPU_TO_CPU_QUEUE = 3
FROM_CPU_TO_IO_QUEUE = 4
FROM_CPU_TO_IO = 5
FROM_CPU_TO_ENDED = 6
FROM_IO_QUEUE_TO_IO = 7
FROM_IO_TO_CPU = 8
FROM_IO_TO_CPU_QUEUE = 9
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
#Format Colors
RANGES = [
    [  "B3:ZZ3", '#FF0000'],
    [  "B4:ZZ4", '#FFB600'],
    [  "B5:ZZ5", '#D3D301'],
    [  "B6:ZZ6", '#97E351'],
    [  "B7:ZZ7", '#00D339'],
    [  "B8:ZZ8", '#00CCB3'],
    [  "B9:ZZ9", '#00B6FF'],
    ["B10:ZZ10", '#0051FF'],
    ["B11:ZZ11", '#3600FF'],
    ["B12:ZZ12", '#8F00FF'],
    ["B13:ZZ13", '#F300FF'],
    ["B14:ZZ14", '#FF00B6'],
    ["B15:ZZ15", '#FF006C'],
    ["B16:ZZ16", '#FF0000'],
]