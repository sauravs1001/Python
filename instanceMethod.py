class SampleClass:
    """sample docstring practice"""
    def __init__(self, data):
        self.data = data

    def printData(self):
        print(self.data)


obj1 = SampleClass('tom')

obj1.printData()

print(SampleClass.__doc__)