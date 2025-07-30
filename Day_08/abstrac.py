# hiding the details and show only require features to the user 

class car:

    def __init__(self,):
        self.acc = False
        self.brk = False
        self.clu = False

    # this run as background not show in output 
    def start(self):
        self.clu = True
        self.acc = True
        print("car starting....")


car_status = car()

car_status.start()
