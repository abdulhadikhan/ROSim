import array

systemVariables = dict()
clock = int()
eventList = dict()


class Car:
    ArrivalTime = 0
    DepartureTime = 0
    DistanceTravelled = 0
    TravelTime = 0
    DeliveryTime = 0
    Status = 0


def carArrivalAtPlant():
    print('ok2')


def bottleFilled():
    print('ok1')


def carLoad():
    print('ok3')


def departFromPlant():
    print('ok4')


def carArrive(self):
    pass


def delieveryPoint(self):
    pass


def bottlesDelievered(self):
    pass


def carDepart(self):
    pass


def cardepartFromStop(self):
    pass


def initialize():
    global systemVariables
    global clock
    global eventList
    systemVariables = {"NoOfWorkers": 3,
                       "NoOfDrivers": 4,
                       "WorkingHours": 6,
                       "NoOfCars": 2,
                       "TimePerBottle": 2,
                       "TimeToUnload": 5,
                       "TimeToLoad": 20,
                       "PricePerBottle": 30,
                       "TotalBottles": 200,
                       "Cars": (Car(), Car()),
                       "Workers": ({"ID": 0, "Worker Status": "none", "Worker Utilization": "Nil"},
                                   {"ID": 1, "Worker Status": "none", "Worker Utilization": "Nil"},
                                   {"ID": 2, "Worker Status": "none", "Worker Utilization": "Nil"}),
                       "Bottlesdelievered": 0,
                       "NumberOfFilledBottles": 0

                       }

    clock = 0
    eventList = {"BottleFilled": systemVariables["TimePerBottle"],
                 "CarArrivalAtPlant": -1,  # -1 = unknown
                 "CarLoaded": -1,
                 "CarDepartFromPlant": -1,
                 "CarArrivedDeliveryPoint": -1,
                 "BottlesDelivered": -1,
                 "CarDepartFromStop": -1
                 }

    timingRoutine()


def smallestPositive(dictionary):
    min = list(dictionary.values())[0]  # hogya bee see
    for value in dictionary.values():
        if (value < min and value >= 0):
            min = value

    return min


# abhi agay iska upyog hoga

def timingRoutine():
    global clock
    global eventList
    clock = smallestPositive(eventList)  # set the clock value to smallest event
    eventRoutine()


def eventRoutine():
    global clock
    global eventList

    if eventList["BottleFilled"] == clock:
        bottleFilled()

    if eventList["CarArrivalAtPlant"] == clock:
        carArrivalAtPlant()

    if eventList["CarLoaded"] == clock:
        carLoad()

    if eventList["CarDepartFromPlant"] == clock:
        carDepart()

    if eventList["CarArrivedDeliveryPoint"] == clock:
        carArrive()

    if eventList["BottlesDelivered"] == clock:
        bottlesDelievered()

    if eventList["CarDepartFromStop"] == clock:
        cardepartFromStop()

    # saaare krne hein is tarah 7 events

#  print(NoOfDrivers, NoOfWorkers, WorkingHours, TimePerBottle, TimeToLoadcar, TimeToUnloadCar)
