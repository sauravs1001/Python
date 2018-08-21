from Oops.oopPractice import Car


class BMW(Car):
    def __init__(self):
        Car.__init__(self)
        print("BMW instance created")


bobj = BMW()
bobj.start()
bobj.stop()

