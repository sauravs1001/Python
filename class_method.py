class SampleClass:
    no_inst = 0

    def __init__(self):
        SampleClass.no_inst = SampleClass.no_inst + 1

    @classmethod
    def get_no_object(cls):
        return cls.no_inst



    # def get_no_of_instances(self, cls_obj):
    #     return cls_obj.no_inst

obj1 = SampleClass()
obj2 = SampleClass()
obj3 = SampleClass()
obj4 = SampleClass()
obj5 = SampleClass()

print(obj4.get_no_object())
