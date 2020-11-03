from Process import Process
import Constants

def has_to_stop(processes):
    for process in processes:
        if not process.has_ended():
            return False
    return True

def cpu_is_empty(processes):
    for process in processes:
        if process.get_state() == Constants.ON_CPU:
            return False
    return True

def io_is_empty(processes):
    for process in processes:
        if process.get_state() == Constants.ON_IO:
            return False
    return True

def get_new_arrivals(processes, time):
    temp = []
    for process in processes:
        if process.get_arrival() == time:
            temp.append(process)
    return temp

def order_by_priority(processes):
    temp = []
    for priority in [Constants.TOP_PRIORITY, Constants.MID_PRIORITY, Constants.LOW_PRIORITY]:
        for process in processes:
            if process.has_priority() and process.get_priority() == priority:
                temp.append(process)
    return temp

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