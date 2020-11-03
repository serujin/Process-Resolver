from Process import Process
import Constants

def has_to_stop(processes):
    temp = True
    for process in processes:
        if not process.has_ended():
            temp = False
    return temp

def get_new_arrivals(processes, time):
    temp = []
    for process in processes:
        if process.get_arrival() == time:
            temp.append(process)
    return temp

def get_processes_ids(processes):
    temp = []
    for process in processes:
        temp.append(process.get_id())
    return temp

def order_by_priority(processes, duration):
    low_priorities = []
    mid_priorities = []
    top_priorities = []
    no_priorities = []
    for process in processes:
        if process.has_priority() and process.get_priority() == Constants.LOW_PRIORITY:
            low_priorities.append(process)
    for process in processes:
        if process.has_priority() and process.get_priority() == Constants.MID_PRIORITY:
            mid_priorities.append(process)
    for process in processes:
        if process.has_priority() and process.get_priority() == Constants.TOP_PRIORITY:
            top_priorities.append(process)
    for process in processes:
        if not process.has_priority():
            no_priorities.append(process)
    low_priorities = order_by_id(low_priorities)
    mid_priorities = order_by_id(mid_priorities)
    top_priorities = order_by_id(top_priorities)
    no_priorities = order_by_id(no_priorities)
    if duration:
        low_priorities = order_by_duration(low_priorities)
        mid_priorities = order_by_duration(mid_priorities)
        top_priorities = order_by_duration(top_priorities)
        no_priorities = order_by_duration(no_priorities)
    return top_priorities + mid_priorities + low_priorities + no_priorities

def order_by_duration(processes):
    possible_durations = []
    durations = []
    for process in processes:
        duration = process.get_duration()
        if not duration in possible_durations:
            possible_durations.append(duration)
    possible_durations.sort()
    for duration in possible_durations:
        temp = []
        for process in processes:
            if process.get_duration() == duration:
                temp.append(process)
        durations += temp
    return durations    
    
def order_by_id(processes):
    ids = []
    for process in processes:
        ids.append(process.get_id())
    ids.sort()
    temp = []
    for _id in ids:
        for process in processes:
            if _id == process.get_id() and process not in temp:
                temp.append(process)
    return temp