from Process import Process
import Utils

processes = [
    Process("a", 10, 20),
    Process("z", 10, 20),
    Process("d", 10, 20),
    Process("e", 10, 20),
    Process("n", 10, 20),
    Process("p", 10, 20),
    Process("z", 10, 20)
]

for p in Utils.order_by_id(processes):
    print(p.show())