import copy

class Routes:
    def __init__(self, d, n, t):
        self.destination = d
        self.nop = n
        self.time = t

    def gettime(self):
      return self.time

    def getdestination(self):
       return self.destination

    def getnop(self):
        return self.nop

    def setnop(self,value):
        self.nop = value

    def __lt__(self, other):
        return self.nop > other.nop


class Drivers:
    def __init__(self, name, available):
        self.name = name
        self.available = available

    def getname(self):
        return self.name


    def getavail(self):
        return self.available


class Buses:
    def __init__(self, name, capacity, available, driver):
        self.name = name
        self.available = available
        self.capacity = capacity
        self.t_moved = 0
        self.driver = driver

    def getname(self):
        return self.name

    def getavail(self):
        return self.available

    def getcapacity(self):
        return self.capacity

    def gettmoved(self):
        return self.t_moved

    def settmoved(self, obj):
        self.t_moved = obj

    def getdriver(self):
        return self.driver

    def setdriver(self, driver):
        self.driver = driver

    def __lt__(self, other):
        return self.t_moved < other.t_moved

class Orderc:
    def __init__(self, order, time):
        self.order = order
        self.time = time

    def getorder(self):
        return self.order

    def gettime(self):
        return self.time

    def __lt__(self, other):
        return self.time < other.time

def addperm(x,l):
    return [ l[0:i] + [x] + l[i:]  for i in range(len(l)+1) ]

def perm(l):
    if len(l) == 0:
        return [[]]
    return [x for y in perm(l[1:]) for x in addperm(l[0],y) ]

def algo(routes, buses, printr):
    tlist = []
    loop=True
    if len(buses) == 0:
        return 0
    routes = sorted(routes)
    buses = sorted(buses)
    key = None
    value = 0
    t1=0
    while loop:
        key = buses[0]
        routes.__getitem__(0).setnop(routes.__getitem__(0).getnop()-key.getcapacity())
        t1 = key.gettmoved()
        key.settmoved(key.gettmoved()+routes.__getitem__(0).gettime())
        if printr:
            v1 = 0
            v2 = 0
            v1 = t1
            v2 = key.gettmoved()
            tlist.append([routes.__getitem__(0).getdestination(),key.getname(),key.getdriver(),v1,v2])
        buses = sorted(buses)
        routes = sorted(routes)
        for obj in routes:
            if obj.getnop() <= 0:
                routes.remove(obj)
        if len(routes) == 0:
            loop = False
    buses = sorted(buses)
    if not printr:
        return buses[len(buses)-1].gettmoved()
    else:
        return tlist

def finder(routes, buses):
    order_times = []
    orders = perm(buses)
    for i in orders:
        cbuses =  copy.deepcopy(i)
        croutes =  copy.deepcopy(routes)
        order_times.append(Orderc(cbuses, algo(croutes, cbuses, False)))
    order_times = sorted(order_times)
    for x in order_times[0].getorder():
        x.settmoved(0)
    return algo(routes, order_times[0].getorder(), True)

#
# class timetable:
#     def __init__(self, destination, bus, dep_time, arr_time):
#         self.destination = destination
#         self.bus = bus
#         self.dep_time = dep_time
#         self.arr_time = arr_time
#
#     def getarr_time(self):
#         return self.arr_time
#
#     def getdep_time(self):
#         return self.dep_time
#
#     def getbus(self):
#         return self.bus
#
#     def getdestination(self):
#         return self.destination