class car:
    def __init__(self, type):
        self.type = type


    @staticmethod
    def start():
        print("car start")

    @staticmethod
    def stop():
        print("car stop")


class abccar(car):
    def __init__(self, name, type):
        self.name = name
        super().__init__(type)


# class toyota(abccar):
#     def __init__(self, brand):
#         self.brand = brand
    

car1  = abccar("prius", "electric")

print(car1.type)

