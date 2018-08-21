class Fruit:
    def __init__(self):
        print("Fruit object is created")

    def nutrition(self):
        print("nutrition value of apple is good")

    def fruit_shape(self):
        print("the shape of Orange is round")


class Orange(Fruit):
    def __init__(self):
        super(Orange, self).__init__()
        print("Now Orange object is created")

    def nutrition(self):
        super().nutrition()
        print("Nutrition value of Orange is also good")

    def color(self):
        print("Guess what is the color of Orange")


frobj = Fruit()
frobj.nutrition()
print("=#=" * 20)
orobj = Orange()
orobj.fruit_shape()
orobj.nutrition()


